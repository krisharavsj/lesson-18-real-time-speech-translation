import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()
print("Choose target language:")
print("1 - Hindi")
print("2 - Tamil")
print("3 - French")
print("4 - Spanish")

choice = input("Enter number: ")
lang_dict = {
    "1": "hi",
    "2": "ta",
    "3": "fr",
    "4": "es"
}

target_lang = lang_dict.get(choice, "hi")  

with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    translated = translator.translate(text, dest=target_lang)
    print("Translated:", translated.text)

except Exception as e:
    print("Error:", e)