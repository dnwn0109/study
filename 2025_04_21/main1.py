# import io
# from google.oauth2 import service_account
# from google.cloud import speech
# import librosa

# client_file = '' # json파일명 넣기
# credentials = service_account.Credentials.from_service_account_file(client_file) #파일 인증?
# client = speech.SpeechClient(credentials=credentials) # 클라이언트 생성

# # Load the audio file
# audio_file = 'C:/coding/recording1.wav' # 테스트용 오디오파일명 넣기
# y,sr = librosa.load(audio_file,sr=None)

# with io.open(audio_file, 'rb') as f: # 바이너리형식으로 읽는구나나
#     content = f.read()
#     audio = speech.RecognitionAudio(content=content) 

# config = speech.RecognitionConfig(
# 	encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz = 44100,
#     language_code = 'ko-KR',
#     audio_channel_count=2
# ) # 이 설정으로 읽나보다다



# response = client.recognize(config=config,audio=audio) # 위에 읽은 오디오랑 컨피그로 클라이언트에서 뭐 하나보다다
# print(response)

# # 너무 인식률이 저조한데 인식률을 늘릴수 있는 방법이 없을까(게임소리에 가려져서 잘 안되는듯)
# # 처음에 구한 wav파일이 모노가 아니여서 ffmpeg를 받고 여기서 변환한 후 사용해야함
# # 다른 방법도 있을까 이건 걍 복붙한 코드라..
# # 





# from pydub import AudioSegment

# sound = AudioSegment.from_wav("C:/coding/한국인 관광객 사망 #Shorts (MBC뉴스).wav")
# sound = sound.set_channels(1)
# sound.export("C:/coding/news.wav", format="wav")


# # 이곳에서 파일을 변환한다 스테레오 > 모노로





# import speech_recognition as sr
# r=sr.Recognizer()
# with sr.Microphone() as source:
#     print('듣고 있어요')
#     audio = r.listen(source)
# try:
#     text = r.recognize_google(audio, language = "en-us")
#     print(text)
#     # text = r.recognize_google(audio, language = "en-kr")
#     # print(text)
# except sr.UnknownValueError:
#     print("인식실패")
# except sr.RequestError as e:
#     print("요청실패:{0}".format(e))

# 이건 따로 api키가 없는데? api가 아니라 그냥 기능을 쓴거 아닌가






from google.cloud import speech
import io
from google.oauth2 import service_account
from google.cloud import speech
from pydub import AudioSegment


from dotenv import load_dotenv
import os
load_dotenv()


import librosa
def change_audio(audio_file : str):
    sound = AudioSegment.from_wav(audio_file)
    sound = sound.set_channels(1)
    sound.export("C:/coding/test_output2.wav", format="wav")



def transcribe_file_with_auto_punctuation(audio_file: str) -> speech.RecognizeResponse:
    """Transcribe the given audio file with auto punctuation enabled.
    Args:
        audio_file (str): Path to the local audio file to be transcribed.
    Returns:
        speech.RecognizeResponse: The response containing the transcription results.
    """
    client_file = os.getenv("GOOGLE_STT_KEY")
    credentials = service_account.Credentials.from_service_account_file(client_file)
    client = speech.SpeechClient(credentials=credentials)
    y,sr = librosa.load(audio_file,sr=None)

    with open(audio_file, "rb") as f:
        audio_content = f.read()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="ko-KR",
        # Enable automatic punctuation
        enable_automatic_punctuation=True,
        audio_channel_count=2,
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
        print(alternative)

    return response

transcribe_file_with_auto_punctuation('C:/coding/recording1.wav')



# from google.cloud import speech
# import io
# from google.oauth2 import service_account

# import pyaudio
# import wave


# def transcribe_file_with_auto_punctuation():
#     """Transcribe the given audio file with auto punctuation enabled.
#     Args:
#         audio_file (str): Path to the local audio file to be transcribed.
#     Returns:
#         speech.RecognizeResponse: The response containing the transcription results.
#     """
#     client_file = '' # json파일명 넣기
#     credentials = service_account.Credentials.from_service_account_file(client_file)
#     client = speech.SpeechClient(credentials=credentials)

    
#     FORMAT = pyaudio.paInt16  # 16비트
#     CHANNELS = 1              # 모노
#     RATE = 48000              # 샘플레이트 (Hz)
#     CHUNK = 1024              # 버퍼 사이즈
#     RECORD_SECONDS = 5        # 녹음 시간 (초)

#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)

#     print("🎙️ 녹음 시작...")

#     frames = []

#     for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)
#     full_data = b''.join(frames)
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()


#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=48000,
#         language_code="ko-KR",
#         # Enable automatic punctuation
#         enable_automatic_punctuation=True,
#     )

#     audio = speech.RecognitionAudio(content=full_data)
#     response = client.recognize(config=config, audio=audio)

#     for i, result in enumerate(response.results):
#         alternative = result.alternatives[0]
#         print("-" * 20)
#         print(f"First alternative of result {i}")
#         print(f"Transcript: {alternative.transcript}")

#     return response


# transcribe_file_with_auto_punctuation()






# from google.cloud import speech
# import io
# from google.oauth2 import service_account
# import pyaudio

# client_file = '' # json파일명 넣기
# credentials = service_account.Credentials.from_service_account_file(client_file)
# client = speech.SpeechClient(credentials=credentials)


# FORMAT = pyaudio.paInt16  # 16비트
# CHANNELS = 1              # 모노
# RATE = 48000              # 샘플레이트 (Hz)
# CHUNK = 1024              # 버퍼 사이즈
# RECORD_SECONDS = 5        # 녹음 시간 (초)
# OUTPUT_FILENAME = "C:/coding/kyo.wav"
# audio = pyaudio.PyAudio()
# stream = audio.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("🎙️ 녹음 시작...")

# frames = []

# for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#     full_data = b''.join(frames)

# audio = speech.RecognitionAudio(content=full_data)

# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=RATE,
#     language_code='ko-KR'
# )

# response = client.recognize(config=config, audio=audio)

# for result in response.results:
#     print("인식 결과:", result.alternatives[0].transcript)











import os
from dotenv import load_dotenv
from google.cloud import speech
from google.oauth2 import service_account

# .env 파일 로드
load_dotenv()

# GCP 인증 파일 경로 불러오기
client_file = os.getenv("GOOGLE_STT_KEY")

# 경로 확인 (디버깅용)
print(f"Client file path: {client_file}")

if client_file is None:
    raise ValueError("GOOGLE_STT_KEY environment variable not set properly!")

# GCP 인증 설정
credentials = service_account.Credentials.from_service_account_file(client_file)

# Google Speech Client 생성
client = speech.SpeechClient(credentials=credentials)
