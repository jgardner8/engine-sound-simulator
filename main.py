import synth
import audio
from engine import Engine

import time

fire_snd = synth.sine_wave_note(200, 0.1)
audio.normalize_volume(fire_snd)
audio.exponential_volume_dropoff(fire_snd, 0.05, 3)
audio.play(fire_snd).wait_done()

thumper = Engine(
    strokes=4,
    cylinders=1,
    timing=[0],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(0.15)
)

parallel_twin = Engine(
    strokes=4,
    cylinders=2,
    timing=[0, 2],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(0.15)
)

v_twin = Engine(
    strokes=4,
    cylinders=2,
    timing=[0, 1],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(0.15)
)

buf = thumper.gen_audio(duration=3)
audio.play(buf).wait_done()

time.sleep(0.1)

buf = parallel_twin.gen_audio(duration=3)
audio.play(buf).wait_done()

time.sleep(0.1)

buf = v_twin.gen_audio(duration=3)
audio.play(buf).wait_done()
