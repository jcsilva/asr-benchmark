#!/usr/bin/env python3

import speech_recognition as sr

from os import path
from sys import argv

if len(argv) != 2:
    print("Usage: " + argv[0] +" <wav_list_file>")
    print()
    print("<wav_list_file> \t is a list with .wav files to be recognized." \
          "Format: one audio per line. ")
    exit()


file_list = argv[1]

r = sr.Recognizer()

with open(file_list, 'r') as audio_list:
    for audio_file in audio_list:

        with sr.AudioFile(audio_file.strip()) as source:
            audio = r.record(source) # read the entire audio file
        # recognize speech using Google Speech Recognition
        try:
            print(audio_file.strip() + '\t' + r.recognize_google(audio, language="pt-BR"), flush=True)
        except sr.UnknownValueError:
            print(" ", flush=True)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e), flush=True)
