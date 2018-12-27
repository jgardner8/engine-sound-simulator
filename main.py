import synth
import audio
from engine import Engine

import time

fire_snd = synth.sine_wave_note(frequency=180, duration=1)
audio.normalize_volume(fire_snd)
audio.exponential_volume_dropoff(fire_snd, duration=0.05, base=3)
audio.play(fire_snd).wait_done()

thumper = Engine(
    strokes=4,
    cylinders=1,
    timing=[0],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

parallel_twin = Engine(
    strokes=4,
    cylinders=2,
    timing=[0, 2],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

v_twin = Engine(
    strokes=4,
    cylinders=2,
    timing=[0, 1],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

inline_four = Engine(
    strokes=4,
    cylinders=4,
    timing=[0, 1, 2, 3],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

print('thumper')
buf = thumper.gen_audio(duration=3)
audio.play(buf).wait_done()

time.sleep(0.1)
print('parallel_twin')
buf = parallel_twin.gen_audio(duration=3)
audio.play(buf).wait_done()

time.sleep(0.1)
print('v_twin')
buf = v_twin.gen_audio(duration=3)
audio.play(buf).wait_done()

time.sleep(0.1)
print('inline_four')
buf = inline_four.gen_audio(duration=3)
audio.play(buf).wait_done()
