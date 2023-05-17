import speech_recognition as sr
import search
import convert
import firstletter

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as source
with sr.Microphone() as source:
    print("Speak now...")
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # capture the audio
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio, language='pa-IN')
    print(f'your voice: {text}')
    convert = convert.unicode(text, True)
    print(f'converted to unicode: {convert} ')
    first_letters = firstletter.first_letters(convert)
    print(f'first letter: {first_letters}')

    search.voice_search(text=first_letters)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


