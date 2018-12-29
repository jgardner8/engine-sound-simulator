import synth
import audio_tools
from audio_device import AudioDevice
from engine import Engine

import signal

fire_snd = synth.sine_wave_note(frequency=180, duration=1)
audio_tools.normalize_volume(fire_snd)
audio_tools.exponential_volume_dropoff(fire_snd, duration=0.05, base=3)

v_twin = Engine(
    strokes=4,
    cylinders=2,
    timing=[0, 1],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

######

def on_sigint(signal, frame):
    try:
        stream.stop_stream()
        stream.close()
        audio_device.close()
    except NameError:
        pass # caught race condition

signal.signal(signal.SIGINT, on_sigint)

audio_device = AudioDevice()
stream = audio_device.play_stream(v_twin.gen_audio)

print('\nPlaying audio...\nPress Ctrl+C to exit')
signal.pause()
