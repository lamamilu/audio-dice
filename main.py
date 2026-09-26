# runs on mac, changes needed to work on rasberry pi
import random
import wave
import subprocess
from piper import PiperVoice

# files needed: 
#    es_ES-sharvard-medium.onnx
#    es_ES-sharvard-medium.onnx.json
voice = PiperVoice.load("es_ES-sharvard-medium.onnx")
user = input()

while True:
     number = random.randint(1,9)

     with wave.open("test.wav", "wb") as wav_file:
          voice.synthesize_wav(str(number), wav_file)

     subprocess.run(["afplay", "test.wav"])
     user = input()


