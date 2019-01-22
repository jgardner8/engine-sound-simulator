import synth
import audio_tools
import controls
from audio_device import AudioDevice
from engine import Engine

fire_snd = synth.sine_wave_note(frequency=160, duration=1)
audio_tools.normalize_volume(fire_snd)
audio_tools.exponential_volume_dropoff(fire_snd, duration=0.06, base=5)

v_twin_90_deg = Engine(
    idle_rpm=1000,
    limiter_rpm=10500,
    strokes=4,
    cylinders=2,
    timing=[0, 180],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

v_twin_60_deg = Engine(
    idle_rpm=1100,
    limiter_rpm=10500,
    strokes=4,
    cylinders=2,
    timing=[0, 120],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

inline_four = Engine(
    idle_rpm=1300,
    limiter_rpm=16500,
    strokes=4,
    cylinders=4,
    timing=[0, 180, 360, 540],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

v_four = Engine(
    idle_rpm=1100,
    limiter_rpm=16500,
    strokes=4,
    cylinders=4,
    timing=[0, 180, 450, 630],
    fire_snd=fire_snd,
    between_fire_snd=synth.silence(1)
)

engine = v_four

######

audio_device = AudioDevice()
stream = audio_device.play_stream(engine.gen_audio)

print('\nEngine is running...')

try:
    controls.capture_input(engine) # blocks until user exits
except KeyboardInterrupt:
    pass

print('Exiting...')
stream.close()
audio_device.close()
