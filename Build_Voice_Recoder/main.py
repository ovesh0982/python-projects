'''
1)import sounddevice as sd: sounddevice library ko import karta hai, jo audio recording ke liye use hota hai.
2)import soundfile as sf: soundfile library ko import karta hai, jo audio ko file format me save karne ke liye use hota hai.
3)from tkinter import *: tkinter library ko import karta hai, jo GUI (Graphical User Interface) banane ke liye istemal hoti hai.
'''



import sounddevice as sd
import soundfile as sf
from tkinter import *


def voice_rec():
  fs = 48000
  duration = int(duration_var.get())
  myrecording = sd.rec(int(duration*fs),samplerate=fs,channels=2)
  sd.wait()
  sf.write('my_audio.flac',myrecording,fs)

  master = Tk()
  master.title("Voice Recorder")
  Label(master,text="Voice Recorder").grid(row=0,sticky=W,rowspan=2)
  Label(master, text="Duration (seconds):").grid(row=1, column=0, sticky=W)
  duration_var = StringVar(value='5')
  Entry(master, textvariable=duration_var).grid(row=1,column=1)
  b = Button(master, text="Start",command=voice_rec)
  b.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
  
  mainloop()

