import synth
import audio

fire_snd = synth.sine_wave_note(200, 0.05)
between_fire_snd = synth.silence(0.05)

buf = audio.concat_notes([fire_snd, between_fire_snd, fire_snd, between_fire_snd, fire_snd])
audio.normalize_volume(buf)

audio.play(buf).wait_done()