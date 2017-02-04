import os
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1 as SpeechToText
from dotenv import load_dotenv
from sys import argv

def transcribe_audio(path_to_audio_file, samplerate):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    username = os.environ.get("BLUEMIX_USERNAME")
    password = os.environ.get("BLUEMIX_PASSWORD")

    speech_to_text = SpeechToText(username=username, password=password)

    if (samplerate == "8000"):
        mdl = "pt-BR_NarrowbandModel"
    elif (samplerate == "16000"):
        mdl = "pt-BR_BroadbandModel"

    with open(path_to_audio_file, 'rb') as audio_file:
        return speech_to_text.recognize(audio_file,
                                       content_type='audio/wav',
                                       max_alternatives=1,
                                       model=mdl)

if __name__ == "__main__":

    if len(argv) != 3:
        print("Usage: " + argv[0] +" <samplerate> <wav_list_file>")
        print()
        print("<samplerate> \t is the audio sampling frequency. All audios in " \
              "the wav_list_file must have the same sampling frequency, " \
              "which must be 8000 or 16000.")
        print("<wav_list_file> \t is a list with .wav files to be recognized." \
              "Format: one audio per line. ")
        exit()

    samplerate = argv[1]
    file_list = argv[2]

    with open(file_list, 'r') as audio_list:
        for audio_file in audio_list:
            audio_file = audio_file.strip()
            if(len(audio_file) != 0):
                response = transcribe_audio(audio_file, samplerate)
                if (len(response) != 0):
                    results = response['results']
                    if (len(results) != 0):
                        alternatives = results[0]['alternatives']
                        if (len(alternatives) != 0):
                            transc = alternatives[0]['transcript']
                            print(audio_file + '\t' + transc, flush=True)
