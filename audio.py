'''Tools to work with audio buffers'''

import cfg

import numpy as np
import simpleaudio as sa

def concat_buffers(bufs):
    return np.hstack(bufs)

def normalize_volume(buf, loudest_sample=None):
    '''Makes the loudest sample in the buffer use the max_16bit volume. No clipping'''
    buf *= cfg.max_16bit / (loudest_sample or find_loudest_sample(buf))

def find_loudest_sample(buf):
    return np.max(np.abs(buf))

def play(buf):
    return sa.play_buffer(buf.astype(np.int16), num_channels=1, bytes_per_sample=2, sample_rate=cfg.sample_rate)
