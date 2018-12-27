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
        timing: array where each element is the number of strokes that cylinder should wait before its
          first fire. Typically first element is 0 so the first cylinder fires right away.
          e.g. Parallel twin 4 stroke timing=[0, 2]
          e.g. 90 deg V-twin 4 stroke timing=[0, 1]
          e.g. Parallel twin 2 stroke timing=[0, 1]
          e.g. Inline four 4 stroke timing=[0, 1, 2, 3]
          e.g. Inline six 4 stroke timing=[0, 4/6, 8/6, 12/6, 16/6, 20/6]
        fire_snd: sound engine should make when a cylinder fires
        between_fire_snd: sound engine should make between cylinders firing
        '''
        self.rpm = 1000

        assert strokes in (2, 4), 'strokes not in (2, 4), see docstring'
        self.strokes = strokes

        assert cylinders > 0, 'cylinders <= 0'
        self.cylinders = cylinders
        assert len(timing) == cylinders, 'len(timing) != cylinders, see docstring'
        self.timing = timing

        assert type(fire_snd) == np.ndarray and \
               type(between_fire_snd) == np.ndarray, \
            'Sounds should be passed in as numpy.ndarray buffers'

        assert len(fire_snd) >= cfg.sample_rate * 0.1 and \
               len(between_fire_snd) >= cfg.sample_rate * 0.1, \
            'Ensure all audio buffers contain at least 0.1 seconds of data, see docstring'
        self.fire_snd = fire_snd
        self.between_fire_snd = between_fire_snd

    def gen_audio(self, duration):
        '''Generate an audio buffer representing the engine running for `duration`'''
        # Calculate durations of fire and between fire events
        strokes_per_min = self.rpm * 2 # revolution of crankshaft is 2 strokes
        fires_per_min = strokes_per_min / self.strokes
        sec_between_fires = 60 / fires_per_min
        fire_duration = sec_between_fires / self.strokes # noise is assumed to be when exhaust valve is open
        between_fire_duration = sec_between_fires / self.strokes * (self.strokes-1) # assumed to be when exhaust valve is closed

        # Take slice of audio buffers based on the duration of sound required
        fire_snd = audio.slice_buffer(self.fire_snd, fire_duration)
        between_fire_snd = audio.slice_buffer(self.between_fire_snd, between_fire_duration)

        # Repeat pattern to fill requested duration
        num_loops = int(duration / sec_between_fires)
        initial_delays = [stroke_delay / strokes_per_min * 60 for stroke_delay in self.timing]

        bufs = []
        for cylinder in range(0, self.cylinders):
            running_snd = [fire_snd, between_fire_snd] * num_loops
            initial_delay_snd = audio.slice_buffer(self.between_fire_snd, initial_delays[cylinder])
            buf = audio.concat_buffers([initial_delay_snd] + running_snd)
            buf = audio.slice_buffer(buf, duration) # make them all the same length even though some started later
            bufs.append(buf)

        return audio.overlay_buffers(bufs)
