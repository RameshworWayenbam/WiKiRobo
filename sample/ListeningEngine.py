import speech_recognition as sr

r = sr.Recognizer()

def listener():
    with sr.Microphone() as source:
        print ('Listening ....!')
        audio = r.listen(source)
        print ('Done!')
    try:
        text = r.recognize_google(audio)
        print(text)
        lang = 'en'

        return text
    except Exception as e:
        print (e)
def main():
    tx =listener();
    print(tx)
if __name__ == "__main__":
    main()  