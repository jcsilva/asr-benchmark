import http.client, urllib.parse, json, os, time
from dotenv import load_dotenv
from sys import argv
from os.path import join, dirname

#subscriptionKey="5fd114d60a5a4b5b8a6bec071bb7d0ee"
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

requestid = os.environ.get("REQUEST_ID")
instanceid = os.environ.get("INSTANCE_ID")
subscriptionKey = os.environ.get("SUBSCRIPTION_KEY")

def getAccessToken():
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Ocp-Apim-Subscription-Key": subscriptionKey,
               "Content-Length": 0 }
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"
    # Connect to server to get the Bing Access Token
    conn = http.client.HTTPSConnection(AccessTokenHost)
    conn.request("POST", path, body=None, headers=headers)
    response = conn.getresponse()

    data = response.read()
    conn.close()
    access_token = data.decode("UTF-8")
    return access_token

def transcribeAudio(path_to_audio_file, samplerate):
    access_token = getAccessToken()
    headers = {"Content-type": "audio/wav; codec=\"audio/pcm\"; samplerate="+samplerate,
               "Authorization": "Bearer " + access_token}

    with open(path_to_audio_file, 'rb') as audio_file:
        response = ""
        try:
            body = audio_file.read()
            #Connect to server to recognize the wave binary
            conn = http.client.HTTPSConnection("speech.platform.bing.com")
            conn.request("POST", "/recognize?scenarios=smd&" \
                  "appid=D4D52672-91D7-4C74-8AD8-42B1D98141A5&" \
                  "locale=pt-BR&" \
                  "device.os=linux&" \
                  "version=3.0&" \
                  "format=json&" \
                  "requestid="+requestid+"&" \
                  "instanceid="+instanceid,
                   body, headers)
            response = conn.getresponse().read().decode("UTF-8")
            conn.close()
        finally:
            audio_file.close()

        return response


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
            response = transcribeAudio(audio_file.strip(), samplerate)
            lexical = ""
            data=json.loads(response)
            if data['header']['status'] == 'success':
                lexical = data['header']['lexical']

            print(audio_file.strip() + '\t' + lexical, flush=True)
