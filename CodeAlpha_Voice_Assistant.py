''' Author- Jagu Manish || Python Programming Internship at CodeAlpha
------------------ TASK 2  - VOICE ASSISTANT -----------------------
Create a custom voice assistant using Python to
personalize and automate tasks according to your
needs. Python's versatility makes it an excellent choice
for scripting and development, allowing you to build a
voice assistant that can compete with the likes of Siri,
Alexa, and Google Assistant.
Tip: Use VS Code for better performance.

'''
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pywhatkit
import random
import shutil
import time
import wikipedia
from threading import Thread
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine_speaking = False


def initialize_reminder_file():
    try:
        with open('reminders.txt', 'r') as file:
            pass
    except FileNotFoundError:
        with open('reminders.txt', 'w') as file:
            pass

initialize_reminder_file()

#female voice
engine.setProperty('volume', 100)
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(text):
    global engine_speaking
    if not engine_speaking:
        engine_speaking = True
        try:
            engine.say(text)
            engine.runAndWait()
        except RuntimeError:
            print("Error: Speech engine is already running.")
        finally:
            engine_speaking = False

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}\n")
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return "None"
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return "None"
        return command.lower()

def respond_to_greeting(command):
    greetings = ["hello", "hi", "hey", "yo"]
    if any(greeting in command for greeting in greetings):
        speak("Hello! My name is Friday! How can I assist you today?")
        return True
    return False

def my_name(command):
    if "your name" in command:
        my_name = "Friday"
        speak(f"My name is {my_name}")
        return True
    return False

def created_by(command):
    if "created you" in command or "who created you" in command:
        created_by = "I was Created by Manish sir."
        speak(created_by)
        return True
    return False

def born(command):
    if "when did you born" in command or "how did you born" in command or "you born" in command:
        reply = "As an AI, I didn't born. I was Programmed!"
        speak(reply)
        return True
    return False

def feelings(command):
    if "have feelings" in command or "do you have feelings" in command:
        have_feelings = '''As an AI, I don't have feelings or emotions.
         I'm a computer program designed to process and generate voice based on the input I receive.
          My responses are based on patterns in data and programming rather than personal experiences or emotions.'''
        speak(have_feelings)
        return True
    return False

def tell_time(command):
    if "what time is it" in command or "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
        return True
    return False

def tell_date(command):
    if "what date is it" in command or "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
        return True
    return False

def how_many(command):
    if "how many days in a month" in command or "days in a month" in command:
        speak("Every month consists of 30 or 31 days, except February. february has 28 or 29 days only, which depends on whether that year is leap year or not.")
    elif "days in a year" in command or "how many days in a year" in command:
        speak("Every year consists of 365 or 366 days, it depends on whether that year is leap year or not.")
    elif "days in february" in command or "how many days in february month" in command:
        speak("In a leap year, february has 29 days or else only 28 days")
        return True
    return False

def tell_day(command):
    if "what day is it" in command or "What day" in command:
        current_day_num = datetime.datetime.now().isoweekday()
        current_day=""
        if current_day_num == 1:
            current_day = "Monday"
        elif current_day_num == 2:
            current_day = "Tuesday"
        elif current_day_num == 3:
            current_day = "Wednesday"
        elif current_day_num == 4:
            current_day = "Thursday"
        elif current_day_num == 5:
            current_day = "Friday"
        elif current_day_num == 6:
            current_day = "Saturday"
        elif current_day_num == 7:
            current_day = "Sunday"
        speak(f"Today is {current_day}")
        return True
    return False

def tell_month(command):
    if "what month is it" in command or "month" in command:
        current_month_num = datetime.datetime.now().month
        current_month =""
        if current_month_num == 1:
            current_month = "January"
        elif current_month_num == 2:
            current_month = "February"
        elif current_month_num == 3:
            current_month = "March"
        elif current_month_num == 4:
            current_month = "April"
        elif current_month_num == 5:
            current_month = "May"
        elif current_month_num == 6:
            current_month = "June"
        elif current_month_num == 7:
            current_month = "July"
        elif current_month_num == 8:
            current_month = "August"
        elif current_month_num == 9:
            current_month = "September"
        elif current_month_num == 10:
            current_month = "October"
        elif current_month_num == 11:
            current_month = "November"
        elif current_month_num == 12:
            current_month = "December"
        speak(f"Current month is {current_month}")
        return True
    return False

def tell_year(command):
    if "what year is it" in command or "year" in command:
        current_year = datetime.datetime.now().year
        speak(f"Current year is {current_year}")
        return True
    return False

def search_web(command):
    if "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return True
        else:
            speak("What would you like to search for?")
            return True
    return False

def open_application(command):
    if "open" in command:
        if "browser" in command:
            speak("Opening web browser")
            webbrowser.open("https://www.google.com")
            return True
        elif "notepad" in command or "text editor" in command:
            speak("Opening text editor")
            os.system("notepad" if os.name == "nt" else "gedit")
            return True
        elif "calculator" in command or "calculate" in command:
            speak("Opening Calculator")
            if os.name == "nt":
                os.system("calc")
            else:
                os.system("gnome-calculator" if shutil.which("gnome-calculator") else "bc")
            return True
        elif "chrome" in command:
            speak("Opening Chrome...")
            try:
                if os.name == "nt":
                    os.startfile("chrome")
                elif os.name == "posix":
                    os.system("google-chrome")
                else:
                    webbrowser.get("chrome").open_new_tab("https://www.google.com")
            except Exception as e:
                speak("Unable to open Chrome. Please make sure it's installed.")
                print(e)
            return True
        elif "brave" in command or "b r a v e" in command:
            speak("Opening Brave browser...")
            try:
                if os.name == "nt":
                    os.startfile("brave")
                elif os.name == "posix":
                    os.system("brave-browser")
                else:
                    webbrowser.get("brave").open_new_tab("https://www.google.com")
            except Exception as e:
                speak("Unable to open Brave. Please make sure it's installed.")
                print(e)
            return True
        elif "settings" in command:
            speak("Opening system settings...")
            try:
                if os.name == "nt":
                    os.system("start ms-settings:")
                elif os.name == "posix":
                    os.system("gnome-control-center")
                else:
                    speak("Unable to open system settings. Please make sure it's supported on your OS.")
            except Exception as e:
                speak("Unable to open system settings.")
                print(e)
            return True
    elif "YouTube" in command:
        speak("Opening YouTube...")
        try:
            webbrowser.open("https://www.youtube.com")
        except Exception as e:
            speak("Unable to open YouTube.")
            print(e)
        return True
    elif "edge" in command.lower():
        speak("Opening Microsoft Edge...")
        try:
            if os.name == "nt":
                os.startfile("msedge")
            elif os.name == "posix":
                os.system("microsoft-edge")
            else:
                webbrowser.get("microsoft-edge").open_new_tab("https://www.google.com")
        except Exception as e:
            speak("Unable to open Microsoft Edge. Please make sure it's installed.")
            print(e)
        return True
    return False


def get_weather(command):
    if "weather" in command or "weather updates" in command or "weather report" in command:
        speak("Please provide a city name")
        city = listen().title()
        if city == 'None':
            return False

        api_key = '[Paste your own OpenWeather API]'
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
        if weather_data.status_code == 200:
            data = weather_data.json()
            status = data['weather'][0]['main']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            speak(f"Weather Conditions in {city}")

            print(f"Temperature: {temp}ºF")
            print(f"Status : {status}")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")

            speak(f"Temperature: {temp} Fahrenheit")
            speak(f"Status : {status}")
            speak(f"Pressure: {pressure} hectopascal")
            speak(f"Humidity: {humidity} percent")
        else:
            speak("Sorry, I couldn't retrieving the weather data. Please check the city name and try again.")
        return True
    return False

def set_reminder(command):
    if "remind me" in command or "set a reminder" in command:
        speak("What should I remind you about?")
        reminder = listen()
        if reminder != "None":
            speak("When should I remind you? Please say the time in HH:MM or HHMM format.")
            reminder_time = listen()
            if reminder_time != "None":
                reminder_time = reminder_time.replace(" ", "")  # Remove any spaces

                # Convert time from HHMM to HH:MM
                if len(reminder_time) == 4 and reminder_time.isdigit():
                    reminder_time = f"{reminder_time[:2]}:{reminder_time[2:]}"
                try:
                    reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M").time()
                    reminder_datetime = datetime.datetime.combine(datetime.datetime.now(), reminder_time)
                    if reminder_datetime < datetime.datetime.now():
                        reminder_datetime += datetime.timedelta(days=1)
                    speak(f"Reminder set for {reminder_datetime.strftime('%Y-%m-%d %H:%M')}")
                    with open('reminders.txt', 'a') as file:
                        file.write(f"{reminder_datetime.strftime('%Y-%m-%d %H:%M')} - {reminder}\n")
                    Thread(target=check_reminder, args=(reminder, reminder_datetime)).start()
                    return True
                except ValueError:
                    speak("I couldn't understand the time format. Please try setting the reminder again.")
                    return False
    return False

def check_reminder(reminder, reminder_datetime):
    while True:
        if datetime.datetime.now() >= reminder_datetime:
            speak(f"Reminder: {reminder}")
            break
        time.sleep(10)

def tell_joke(command):
    if "joke" in command:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!", "What do kids play when their mom is using the phone? Bored games.",
                "What do you call an ant who fights crime? A vigilANTe!" , "Why are snails slow? Because they’re carrying a house on their back.", " What’s the smartest insect? A spelling bee!",
                "What does a storm cloud wear under his raincoat? Thunderwear.", "What is fast, loud and crunchy? A rocket chip.", "What do you call a couple of chimpanzees sharing an Amazon account? PRIME-mates.",
                "Why did the teddy bear say no to dessert? Because she was stuffed.", "Why did the soccer player take so long to eat dinner? Because he thought he couldn’t use his hands.",
                "Name the kind of tree you can hold in your hand? A palm tree!", "What has ears but cannot hear? A cornfield.", "What’s a cat’s favorite dessert? A bowl full of mice-cream.",
                'What did the policeman say to his hungry stomach? “Freeze. You’re under a vest.”', "What did the left eye say to the right eye? Between us, something smells!",
                "What do you call a guy who’s really loud? Mike.", "Why do birds fly south in the winter? It’s faster than walking!", "What did the lava say to his girlfriend? 'I lava you!'",
                "Why did the student eat his homework? Because the teacher told him it was a piece of cake.", "What did Yoda say when he saw himself in 4k? HDMI.",
                "What’s Thanos’ favorite app on his phone? Snapchat.", "Sandy’s mum has four kids; North, West, East. What is the name of the fourth child? Sandy, obviously!",
                "What is a room with no walls? A mushroom.", 'What did one math book say to the other? “I’ve got so many problems.”', "What do you call two bananas on the floor? Slippers.",
                "A plane crashed in the jungle and every single person died. Who survived? Married couples.", "What do you call a Star Wars droid that takes the long way around? R2 detour.",
                "What goes up and down but doesn’t move? The staircase."]
        random_joke = random.choice(jokes)
        speak(random_joke)
        return True
    return False

def play_rhyme(command):
    rhymes =["""Baa, baa black sheep
Have you any wool
Yes sir, yes sir
Three bags full.

One for my master
And one for my dame
And one for the little boy
Who lives down the lane.""",
             """Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the King’s horses and all the King’s men,
Couldn’t put Humpty together again.""",
             """Jack and Jill went up the hill
To fetch a pail of water.
Jack fell down and broke his crown,
And Jill came tumbling after.

Up Jack got and home did trot
As fast as he could caper;
And went to bed to mend his head
With vinegar and brown paper.""",
             """Old MacDonald had a farm, E I E I O,
And on his farm he had a cow, E I E I O.
With a moo moo here and a moo moo there,
Here a moo, there a moo, everywhere a moo moo.
Old MacDonald had a farm, E I E I O.""",
             """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night."""]
    if "poem" in command or "poetry" in command or "poem" in command or "nursery rhyme" in command or "kid's rhyme" in command or "rhyme" in command:
        selected_rhyme = random.choice(rhymes)
        speak(selected_rhyme)
        return True
    return False

def play_yt_video(command):
    if 'play' in command or "on youtube" in command or "youtube" in command:
        speak('Opening YouTube...')
        query = command.replace('play', '').strip()
        pywhatkit.playonyt(query)
        return True
    return False

def answer_question(command):
    if "who is" in command or "who was" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "").replace("who was", "").strip()
        if query:
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(f"Here is what I found: {result}")
                return True
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple meanings. Please be more specific.")
                print(f"DisambiguationError: {e.options}")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any information on that topic.")
            except wikipedia.exceptions.WikipediaException as e:
                speak("Sorry, I couldn't retrieve the information.")
                print(f"WikipediaException: {e}")
    return False

def main():
    while True:
        command = listen()
        if command == "None":
            continue

        if "stop" in command or "bye" in command:
            speak("Good bye..! See you later!")
            break

        if my_name(command):
            continue

        if created_by(command):
            continue

        if feelings(command):
            continue

        if born(command):
            continue

        if respond_to_greeting(command):
            continue

        if how_many(command):
            continue

        if tell_day(command):
            continue

        if tell_year(command):
            continue

        if tell_month(command):
            continue

        if tell_time(command):
            continue

        if tell_date(command):
            continue

        if search_web(command):
            continue

        if open_application(command):
            continue

        if get_weather(command):
            continue

        if set_reminder(command):
            continue

        if tell_joke(command):
            continue

        if play_rhyme(command):
            continue

        if play_yt_video(command):
            continue

        if answer_question(command):
            continue

        speak("Sorry, I can't help with that.")


hour = datetime.datetime.now().hour
if 0 <= hour < 12:
    va_greeting = "Good Morning!"
elif 12 <= hour < 16:
    va_greeting = "Good Afternoon!"
else:
    va_greeting = "Good Evening!"

speak(f"{va_greeting} Voice assistant activated. How can I help you?")
main()
