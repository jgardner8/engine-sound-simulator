'''Basic simulation of engine for purposes of audio generation'''

import cfg
import audio

import numpy as np

class Engine:
    def __init__(self, strokes, cylinders, timing, fire_snd, between_fire_snd):
        '''
        Note: all sounds used will be concatenated to suit engine run speed.
        Make sure there's excess audio data available in the buffer.

        strokes: number of strokes in full engine cycle, must be 2 or 4
        cylinders: number of cylinders in engine
        timing: array where each element is the number of strokes before the next cylinder fires
        fire_snd: sound engine should make when a cylinder fires
        between_fire_snd: sound engine should make between cylinders firing
        '''
        self.rpm = 1000

        assert strokes in (2, 4), 'strokes not in (2, 4), see docstring'

        assert cylinders > 0, 'cylinders <= 0'
        self.cylinders = cylinders
        assert len(timing) == cylinders, 'len(timing) != cylinders, see docstring'
        self.timing = timing

        assert type(fire_snd) == np.ndarray and \
               type(between_fire_snd) == np.ndarray, \
            'Sounds should be passed in as numpy.ndarray buffers'

        assert len(fire_snd) >= cfg.sample_rate / 4 and \
               len(between_fire_snd) >= cfg.sample_rate / 4, \
            'Ensure all audio buffers contain at least 0.25 seconds of data, see docstring'
        loudest_sample = max([
            audio.find_loudest_sample(fire_snd),
            audio.find_loudest_sample(between_fire_snd)
        ])
        audio.normalize_volume(fire_snd, loudest_sample)
        audio.normalize_volume(between_fire_snd, loudest_sample)
        self.fire_snd = fire_snd
        self.between_fire_snd = between_fire_snd

    def gen_audio(self, duration):
        '''Generate an audio buffer representing the engine running for `duration`'''
        buf = audio.concat_notes([
            self.fire_snd,
            self.between_fire_snd,
            self.fire_snd,
            self.between_fire_snd,
            self.fire_snd
        ])

        return buf
