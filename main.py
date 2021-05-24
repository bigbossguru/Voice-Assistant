import pyttsx3
from datetime import datetime
import speech_recognition as sr
import smtplib

# global variables
speed_speech = 120


# main function 
def main():
    # speak("Hello Elvera, How are you?")
    
    send_email('Hello Test', 'Hello workld, good', 'yandex')

    while False:
        query = take_command()
        if 'good' in query:
            speak('Have a nice day')
        elif 'bad' in query:
            speak('I love you')
        elif 'fine' in query:
            speak('Ok, Baby')
        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = take_command()
                send_email(content)
                speak('Sent good')
            except Exception as e:
                speak(e)

        elif 'exit' in query:
            exit()

def send_email(title, msg, host):
    dict_smtp = {
        'google': {'smtp':'smtp.google.com', 'port': 587},
        'yandex': {'smtp':'smtp.yandex.ru', 'port': 465}
    }
    server = smtplib.SMTP_SSL(dict_smtp['yandex']['smtp'], dict_smtp['yandex']['port'])
    server.ehlo()
    if 'google' in host: server.starttls()
    message = 'Subject: {}\n\n{}'.format(title,msg)
    server.login('egazizov.eldar@yandex.ru', '7S6JVN9ppr')
    server.sendmail(from_addr='egazizov.eldar@yandex.ru', to_addrs='egazizov.eldar@yandex.ru', msg=message)
    server.close()

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
    with sr.Microphone(device_index=1) as source:
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