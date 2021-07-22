import base64
import pip
import json
import websocket 
import ibm_cloud_sdk_core
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#create variables
apikey ='ydlOLWVW-sQd4JCfDyBzAWb7geCsrarVZcv9oZzit7r'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/56137b4c-f7ae-47bf-bde8-e16669fdff9b'
# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)
#convert from text -welcoming text-
with open('./speech.mp3', 'wb') as audio_file: #Write only mode.
    res = tts.synthesize('welcome customer', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
#read file -convert from .txt file- 
with open('text.txt', 'r') as f: 

    text1 = f.readlines()
    text1 = [line.replace('\n','') for line in text1]
    text1 = ''.join(str(line) for line in text1)

with open('./speech2.mp3', 'wb') as audio_file:
    res = tts.synthesize(text1, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)