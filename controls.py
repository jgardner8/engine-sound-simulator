import time
import inputs
import threading

def _key_events():
    events = inputs.get_key()
    return filter(lambda e: e.ev_type == 'Key', events)

class _BlockingInputThread(threading.Thread):
    '''
    The `inputs` library's IO is blocking, which means a new thread is needed to wait for
    events to avoid blocking the program when no inputs are received.
    '''
    def __init__(self, lock):
        super(_BlockingInputThread, self).__init__(daemon=True)
        self.lock = lock
        self.space_held = False

    def run(self):
        while True:
            for event in _key_events():
                if event.code == 'KEY_SPACE':
                    with self.lock:
                        self.space_held = bool(event.state)

def capture_input(engine):
    print('Press Ctrl+C to exit, Space to rev\n')

    lock = threading.Lock()
    blockingInputThread = _BlockingInputThread(lock)
    blockingInputThread.start()

    while True:
        with lock:
            engine.throttle(1.0 if blockingInputThread.space_held else 0.0)

        time.sleep(0.02)
