"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
from google.oauth2 import service_account
from dotenv import load_dotenv
import os
load_dotenv()


# Instantiates a client
client_file = os.getenv("GOOGLE_TTS_KEY") # json파일명 넣기
credentials = service_account.Credentials.from_service_account_file(client_file)
client = texttospeech.TextToSpeechClient(credentials=credentials)

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="오늘 운동 가 말아ㅠㅜㅠㅠㅠ")
# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    # audio_encoding=texttospeech.AudioEncoding.LINEAR16
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("C:/coding/test4.wav", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

import librosa
audio_path = 'C:/coding/test.wav'
y,sr = librosa.load(audio_path)


import sys
import os
sys.path.append(os.path.abspath('C:/coding/2025_04_21/'))
from main1 import change_audio, transcribe_file_with_auto_punctuation

# change_audio('C:/coding/test.wav')

a = transcribe_file_with_auto_punctuation('C:/coding/test4.wav')
# print(a)
# print('='*100)
# print('='*100)
# print(a.results)
# print('='*100)
print(a.results[0].alternatives[0].transcript)
b = a.results[0].alternatives[0].transcript


## 파일 저장하기기
import pickle

with open('C:/coding/file.txt','wb') as f:
    pickle.dump(b, f)

with open('C:/coding/file2.txt', 'w', encoding='utf-8') as f:
    f.write(str(b)) 

import json

with open('C:/coding/file1.txt', 'w', encoding='utf-8') as f:
    json.dump(b, f, ensure_ascii=False)