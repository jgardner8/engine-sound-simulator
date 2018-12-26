'''Synthesisation of primitive audio building blocks'''

import cfg

import numpy as np

def sine_wave_note(frequency, duration):
    '''
    Creates audio buffer representing a sine-wave
    frequency: Hz
    duration: seconds
    '''
    elements = int(duration * cfg.sample_rate)
    timesteps = np.linspace(start=0, stop=duration, num=elements, endpoint=False)
    return np.sin(frequency * timesteps * 2 * np.pi)

def silence(duration):
    '''
    Creates audio buffer representing silence
    duration: seconds
    '''
    elements = int(duration * cfg.sample_rate)
    return np.zeros(elements)
