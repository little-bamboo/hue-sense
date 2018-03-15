# source activate -my environment name-
# brew install portaudio
# pip install pyaudio

import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 4000
with sr.Microphone(device_index=2, sample_rate=32000, chunk_size=512) as source:
  print'listening'
  audio = r.listen(source)
  print'processing'

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
