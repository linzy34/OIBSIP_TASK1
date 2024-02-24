import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

voice_recognizer = sr.Recognizer()
text_to_speech_engine = pyttsx3.init('sapi5')
voices = text_to_speech_engine.getProperty('voices')
text_to_speech_engine.setProperty('voice', voices[1].id)


def speak(text):
    text_to_speech_engine.say(text)
    text_to_speech_engine.runAndWait()


def greeting():
    current_hr = int(datetime.datetime.now().hour)
    if 0 <= current_hr < 12:
        speak("Good Morning!")
    elif 12 <= current_hr < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello, I am your voice assistant. How can I help you today?")


def get_input():
    with sr.Microphone() as source:
        print("Listening...")
        voice_recognizer.threshold=1
        audio = voice_recognizer.listen(source)

    try:
        print("Recognizing...")
        query = voice_recognizer.recognize_google(audio)
        print(f"You said: {query}\n")

    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return ""
    return query


def main():
    greeting()
    while True:
        query = get_input()

        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Now... The time is {current_time}")
        elif "date" in query:
            today_date = datetime.datetime.now().strftime("%m-%d-%Y")  # Corrected the date format
            speak(f"Today is {today_date}.")
        elif "search" in query:
            speak("What do you want to search for?")
            search_query = get_input()
            if search_query:
                url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
                webbrowser.open(url)
                speak("Here are the results based on your search.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")


if __name__ == "__main__":
    main()
