from translate import Translator
import speech_recognition as sr
import pyaudio
from gtts import gTTS
from playsound import playsound

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Silence please!")
    print("Speak now:")
    audio=r.listen(source)
    try:
        speech_text=r.recognize_google(audio, language='ta')
        print(speech_text)
    except sr.UnknownValueError:
        print("Couldn't Understand!")
    except sr.RequestError:
        print("Couldn't request result from Google")

    translator= Translator(to_lang="en", from_lang='ta')
    translation = translator.translate(speech_text)
    print(translation)

    voice=gTTS(translation, lang='en')
    voice.save("voice.mp3")
    playsound("voice.mp3")
