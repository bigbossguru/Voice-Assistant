import pyttsx3
from datetime import datetime
import speech_recognition as sr
from lib_conf import eemail

# global variables
speed_speech = 120

# main function 
def main():
    # First greeting
    speak("Hello Sir!, How are you?")
    try:
        while True:
            query = take_command()
            if 'time' in query:
                time_and_date()
            elif 'bad' in query:
                speak('I love you')
            elif 'fine' in query:
                speak('Ok, Baby')
            elif 'send email' in query:
                try:
                    speak('Who should I write tell me the name')
                    name = take_command()
                    speak('What should I write?')
                    content = take_command()
                    eemail.send_email(title='Email from Voice Assistant', name=name, msg=content, host='yandex')
                    speak('Sent good')
                except Exception as e:
                    speak(e)

            elif 'exit' in query:
                exit()
    except KeyboardInterrupt: print('Stop Voice Assistant')

def speak(audio=None):

    # initialize speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', speed_speech)
    
    engine.say(audio)
    engine.runAndWait()

def time_and_date():

    day = datetime.today().weekday()+1
    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)

    now = datetime.now()
    date_now = now.strftime("%d of %B, %Y")
    speak(f'Date is it today: {day_of_week} {date_now}')

def take_command():
    voice_recognition = sr.Recognizer()
    with sr.Microphone(device_index=1) as source: #device_index=1 find index in mic.py
        print("Listening...")
        voice_recognition.pause_threshold = 1
        audio = voice_recognition.listen(source)
    try:
        print("Recognizing...")
        query = voice_recognition.recognize_google(audio_data=audio, language='en-US')
        print(query)
        return query
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return


if __name__ == "__main__":
    main()
