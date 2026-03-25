import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr
from scipy.io.wavfile import write

fs = 44100 
seconds = 5

print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("output.wav", fs, recording)

plt.plot(recording)
plt.title("Waveform")
plt.show()

recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Text:", text)
except:
    print("Could not understand audio")