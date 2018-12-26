'''Tools to work with audio buffers'''

import cfg

import numpy as np
import simpleaudio as sa

def concat_notes(notes):
    return np.hstack(notes)

def normalize_volume(buf):
    '''Makes the loudest sound in the buffer use the max_16bit volume. No clipping'''
    buf *= cfg.max_16bit / np.max(np.abs(buf))

def play(buf):
    return sa.play_buffer(buf.astype(np.int16), num_channels=1, bytes_per_sample=2, sample_rate=cfg.sample_rate)