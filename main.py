import numpy as np
import simpleaudio as sa

sample_rate = 44100
max_16bit = 32767

def sine_wave_note(frequency, duration):
    '''
    Creates audio buffer representing a sine-wave
    frequency: Hz
    duration: seconds
    '''
    elements = int(duration * sample_rate)
    timesteps = np.linspace(start=0, stop=duration, num=elements, endpoint=False)
    return np.sin(frequency * timesteps * 2 * np.pi)

def concat_notes(notes):
    return np.hstack(notes)

def normalize_volume(buf):
    '''Makes the loudest sound in the buffer use the max_16bit volume. No clipping'''
    buf *= max_16bit / np.max(np.abs(buf))

def play(buf):
    return sa.play_buffer(buf.astype(np.int16), num_channels=1, bytes_per_sample=2, sample_rate=sample_rate)

a_note = sine_wave_note(440, 0.25)
csharp_note = sine_wave_note(440 * 2 ** (4 / 12), 0.25)
e_note = sine_wave_note(440 * 2 ** (7 / 12), 0.25)

buf = concat_notes([a_note, csharp_note, e_note])
normalize_volume(buf)

play(buf).wait_done()