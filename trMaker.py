#import library
import pyttsx3
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
while True:
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration= 0.2)
            audio = r.listen(mic)
            text =  r.recognize_google(audio)
            
            # using google speech recognition
            print(f"Recognized {text}")

    except :
        r = sr.Recognizer()
        continue