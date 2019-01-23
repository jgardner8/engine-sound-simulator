# Reference: https://en.wikipedia.org/wiki/Big-bang_firing_order

import synth
import audio_tools
from engine import Engine

_fire_snd = synth.sine_wave_note(frequency=160, duration=1)
audio_tools.normalize_volume(_fire_snd)
audio_tools.exponential_volume_dropoff(_fire_snd, duration=0.06, base=5)

def v_twin_90_deg():
    '''Suzuki SV650/SV1000, Yamaha MT-07'''
    return Engine(
        idle_rpm=1000,
        limiter_rpm=10500,
        strokes=4,
        cylinders=2,
        timing=[270, 450],
        fire_snd=_fire_snd,
        between_fire_snd=synth.silence(1)
    )

def v_twin_60_deg():
    return Engine(
        idle_rpm=1100,
        limiter_rpm=10500,
        strokes=4,
        cylinders=2,
        timing=[300, 420],
        fire_snd=_fire_snd,
        between_fire_snd=synth.silence(1)
    )

def v_twin_45_deg():
    return Engine(
        idle_rpm=800,
        limiter_rpm=7000,
        strokes=4,
        cylinders=2,
        timing=[315, 405],
        fire_snd=_fire_snd,
        between_fire_snd=synth.silence(1)
    )

def inline_four():
    return Engine(
        idle_rpm=1300,
        limiter_rpm=16500,
        strokes=4,
        cylinders=4,
        timing=[180, 180, 180, 180],
        fire_snd=_fire_snd,
        between_fire_snd=synth.silence(1)
    )

def v_four_90_deg():
    return Engine(
        idle_rpm=1100,
        limiter_rpm=16500,
        strokes=4,
        cylinders=4,
        timing=[180, 90, 180, 270],
        fire_snd=_fire_snd,
        between_fire_snd=synth.silence(1)
    )
