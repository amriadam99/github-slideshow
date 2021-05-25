from gtts import gTTS
import playsound
import urllib3

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

urllib3.disable_warnings()
speak("hello tim")
