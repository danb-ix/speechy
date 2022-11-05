from pedalboard import Pedalboard, Chorus, Reverb, Compressor, Gain, LadderFilter, Phaser, Delay, PitchShift
from pedalboard.io import AudioFile
with AudioFile('sound.mp3') as f:
  audio = f.read(f.frames)
  samplerate = f.samplerate
print('\n')
board = Pedalboard([
])
print('Chorus, Reverb, Compressor, Gain, HPF, Phaser, Delay, Pitchshift 6ST, PitchShift 12ST, PitchShift Minus 6ST, PitchShift Minus 12ST \n')
whatEffect = input('What effects would you like? ').lower()

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
  board.append(Delay(delay_seconds=0.1, mix=1.0))


def pitchshift6ST():
  board.append(PitchShift(semitones=6))

def pitchshift12ST():
  board.append(PitchShift(semitones=12))

def pitchshiftMinus6ST():
  board.append(PitchShift(semitones=-6))

def pitchshiftMinus12ST():
  board.append(PitchShift(semitones=-12))

e = whatEffect.split(", ")

effects = {
  "chorus" : chorus,
  "reverb" : reverb,
  "compressor" : compressor,
  "gain" : gain,
  "hpf" : ladderfilter,
  "phaser" : phaser,
  "delay" : delay,
  "pitchshift 6st" : pitchshift6ST,
  "pitchshift 12st" : pitchshift12ST,
  "pitchshift minus 6st" : pitchshiftMinus6ST,
  "pitchshift minus 12st" : pitchshiftMinus12ST,
}


for x in e:
    try:
        plugin = effects[x]
    except KeyError:
        print(f'"{x}" is not in the effect list, are you sure you spelt it correctly?')
        continue # Skip to next one; prevent code below from running

    plugin()


effected = board(audio, samplerate)
with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
  f.write(effected)
  print('Audio successfully effected, you can find it at "processed-output.wav"')