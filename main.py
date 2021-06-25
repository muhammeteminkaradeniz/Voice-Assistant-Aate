import os
import time
import playsound
import speech_recognition  as sr
from gtts import gTTS
import webbrowser
import pyfiglet
import sys
from PIL import Image


print("-" * 60)
banner=pyfiglet.figlet_format('Aate')
print(banner)
print(' (c) Emin Karadeniz. All rights reserved.')
print("-" * 60)


########   TEXT ---->> SPEACH ##########
def speak(text):
    tts=gTTS(text=text, lang='en', tld='co.uk')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said="" 

        try:
            said=r.recognize_google(audio)
            print(said)

        except Exception as e:
            speak('I am sorry,i did not get what you say')

    return said

speak('Welcome What is your oreder ?')

while True:
    text=get_audio()

    if 'hello' in text:
        speak('Hello, how are you')

    if 'i am fine' in text:
        speak('Good to hear that')
    if 'how is your day' in text:
        speak('I am just trying be more cleaver.I am working and learning,you should too')
    if 'who made you' in text:
        speak('Emin Karadeniz is my creator.He is smart and handsome, ahahaha, that was joke')

    if 'open Google' in text:
        url_stretch="https://google.com.tr/"
        webbrowser.open_new_tab(url_stretch)
        time.sleep(1)
        speak('here it is,google ')
          
    if 'thank you' in text:
        speak('You are welcome. I am always here for help you') 
    
    if 'goodbye' in text:
        speak('okey see you later')
        sys.exit()

