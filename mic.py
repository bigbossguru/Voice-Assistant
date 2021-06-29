import speech_recognition as sr

mic = sr.Microphone()
print(mic.list_microphone_names()[1])