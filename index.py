from pedalboard import Pedalboard, Chorus, Reverb, Compressor, Gain, LadderFilter, Phaser, Delay, Distortion, PitchShift, Mix
from pedalboard.io import AudioFile
with AudioFile('sound.mp3') as f:
  audio = f.read(f.frames)
  samplerate = f.samplerate
board = Pedalboard([
])

effect1 = input('What effects would you like? ').lower()

def chorus():
  board.append(Chorus())

def reverb():
  board.append(Reverb(room_size=0.25))

def compressor():
  board.append(Compressor(threshold_db=-50, ratio=25))

def gain():
  board.append(Gain(gain_db=12))

def ladderfilter():
  board.append(LadderFilter(mode=LadderFilter.Mode.HPF12, cutoff_hz=1000))

def phaser():
  board.append(Phaser())

def delay():
  board.append(Delay(delay_seconds=0.25, mix=1.0))

def distortion():
  board.append(Distortion)

def pitchshift6ST():
  board.append(PitchShift(semitones=6))

def pitchshift12ST():
  board.append(PitchShift(semitones=12))

def pitchshiftMinus6ST():
  board.append(PitchShift(semitones=-6))

def pitchshiftMinus12ST():
  board.append(PitchShift(semitones=-12))

effected = board(audio, samplerate)
with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
  f.write(effected)
