'''Tools to work with audio buffers'''

import cfg

import numpy as np
import simpleaudio as sa

def concat_buffers(bufs):
    return np.hstack(bufs)

def overlay_buffers(bufs):
    assert type(bufs) == list and len(bufs), 'bufs must be a non-empty list'
    assert all(len(bufs[0]) == len(buf) for buf in bufs), 'All buffers must have the same length'

    bufs = [np.copy(buf) for buf in bufs]
    for buf in bufs:
        buf / len(bufs)

    out_buf = np.empty(len(bufs[0]))
    out_buf = np.sum(bufs, axis=0)
    normalize_volume(out_buf)

    return out_buf

def normalize_volume(buf, loudest_sample=None):
    '''Makes the loudest sample in the buffer use the max_16bit volume. No clipping'''
    buf *= cfg.max_16bit / (loudest_sample or find_loudest_sample(buf))

def find_loudest_sample(buf):
    return np.max(np.abs(buf))

def slice_buffer(buf, duration):
    '''Take slice of audio buffers based on the duration of sound required'''
    num_samples = int(duration * cfg.sample_rate)
    return buf[:num_samples]

def play(buf):
    return sa.play_buffer(buf.astype(np.int16), num_channels=1, bytes_per_sample=2, sample_rate=cfg.sample_rate)
