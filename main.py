import synth
import audio
from engine import Engine

engine = Engine(
    strokes=4,
    cylinders=1,
    timing=[1],
    fire_snd=synth.sine_wave_note(200, 0.25),
    between_fire_snd=synth.silence(0.25)
)

buf = engine.gen_audio(duration=3)
audio.play(buf).wait_done()
