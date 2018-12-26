import synth
import audio
from engine import Engine

import time

thumper = Engine(
    strokes=4,
    cylinders=1,
    timing=[0],
    fire_snd=synth.sine_wave_note(200, 0.25),
    between_fire_snd=synth.silence(0.25)
)

parallel_twin = Engine(
    strokes=4,
    cylinders=2,
    timing=[0, 2],
    fire_snd=synth.sine_wave_note(200, 0.25),
    between_fire_snd=synth.silence(0.25)
)

v_twin = Engine(
    strokes=4,
    cylinders=2,
    timing=[0, 1],
    fire_snd=synth.sine_wave_note(200, 0.25),
    between_fire_snd=synth.silence(0.25)
)

buf = thumper.gen_audio(duration=3)
audio.play(buf).wait_done()

time.sleep(1)

buf = parallel_twin.gen_audio(duration=3)
audio.play(buf).wait_done()

time.sleep(1)

buf = v_twin.gen_audio(duration=3)
audio.play(buf).wait_done()
