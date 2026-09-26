import random
import wave
import subprocess
from piper import PiperVoice

voice = PiperVoice.load("es_ES-sharvard-medium.onnx")
user = input()

while True:
     number = random.randint(1,9)

     with wave.open("test.wav", "wb") as wav_file:
          voice.synthesize_wav(str(number), wav_file)

     subprocess.run(["afplay", "test.wav"])
     user = input()