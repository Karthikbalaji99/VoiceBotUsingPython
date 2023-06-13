#import necessary libraries

import pyttsx3
import speech_recognition as sr
import requests
import subprocess
import random
import string
import pygame


API_KEY = '...' #add your own opeenweather api key
shazam_key = '...' #add your own shazam api key
JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"
SHAZAM_API_URL = 'https://shazam.p.rapidapi.com'
RIDDLE_API_URL = "https://riddles-api.vercel.app/random"


#initialise to take commands as voice input from the user

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio)
            print("The query is:", query)
        except Exception as e:
            print(e)
            print("Say that again, please")
            return "None"
    return query

#define and alert the program about when to speak
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

#defining to get the weather in a city
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data["cod"] == "404":
        return None
    else:
        weather_info = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }
        return weather_info

#defining to make the program tell a random joke
def get_random_joke():
    response = requests.get(JOKE_API_URL)
    data = response.json()
    if response.status_code == 200 and data["type"] == "single":
        joke = data["joke"]
        return joke
    elif response.status_code == 200 and data["type"] == "twopart":
        setup = data["setup"]
        delivery = data["delivery"]
        joke = f"{setup} {delivery}"
        return joke
    else:
        return None
    

#defining to make the program tell a random riddle    
def get_random_riddle():
    response = requests.get(RIDDLE_API_URL)
    data = response.json()
    if response.status_code == 200 and "riddle" in data and "answer" in data:
        riddle = data["riddle"]
        answer = data["answer"]
        riddle_text = f"Riddle: {riddle}\nAnswer: {answer}"
        return riddle_text
    else:
        return None

#defining to make the program define a word given as inout by the user
def get_dictionary_definition(term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    headers = {
        "X-RapidAPI-Key": "....", #use your own api key
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    params = {
        "term": term
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if response.status_code == 200 and "list" in data:
            definitions = data["list"]
            if len(definitions) > 0:
                # Get the first definition from the list
                definition = definitions[0]["definition"]
                return definition
        return None
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None


#this code allows you to convert whatver you say into text and even print it so that you can copy it later.
def convert_speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Starting')
        r.pause_threshold = 10
        audio = r.listen(source)
        try:
            print("Analyzing")
            text = r.recognize_google(audio)
            print("Speech to Text:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the speech.")
        except sr.RequestError as e:
            print("Sorry, speech recognition service is not available. Error: ", e)
    return None

#this allows us to translate text to any language and even print the translated text
def translate_text(text, target_language, source_language=None):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "...",  #use your own api key
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    data = {
        "q": text,
        "target": target_language
    }
    if source_language:
        data["source"] = source_language

    try:
        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()
        if response.status_code == 200 and "data" in response_data and "translations" in response_data["data"]:
            translations = response_data["data"]["translations"]
            if len(translations) > 0 and "translatedText" in translations[0]:
                translated_text = translations[0]["translatedText"]
                return translated_text
        return None
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None
    
#this requires the script to run in admin mode
def mute_sound():
    # Mute the laptop's sound
    engine = pyttsx3.init()
    # Set the system volume to 0 (mute)
    engine.setProperty('volume', 0)
    # Save and apply the changes
    engine.save_to_file('', 'mute_sound.reg')
    subprocess.call(['regedit', '/s', 'mute_sound.reg'])

#this requires the script to run in admin mode
def enable_airplane_mode():
    # Enable airplane mode using subprocess
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=disable'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'name="Bluetooth"', 'admin=disable'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'name="Cellular"', 'admin=disable'])

#to calculate different expressions
def calculate_expression(expression):
    url = "https://big-numbers-calculation.p.rapidapi.com/api/do"
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "....", #use your own api key
        "X-RapidAPI-Host": "big-numbers-calculation.p.rapidapi.com"
    }
    data = {
        "query": expression
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()["body"]
        print("Result:", result)
    except Exception as e:
        print("Error occurred:", e)
        
#this code generates a random password of said length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#we can play a snake game
def play_snake_game():
    pygame.init()

    # Colors
    white = (255, 255, 255) # rgb format
    red = (255, 0, 0)
    black = (0, 0, 0)

    # Creating window
    screen_width = 900
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

    # Game Title
    pygame.display.set_caption("Coders Home")
    pygame.display.update()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)

    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x,y])

    def plot_snake(gameWindow, color, snk_list, snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

    # Game Loop
    def gameloop():
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1

        food_x = random.randint(20, screen_width-20)
        food_y = random.randint(60, screen_height -20)
        score = 0
        init_velocity = 4
        snake_size = 30
        fps = 60   # fps = frames per second
        while not exit_game:
            if game_over:
                gameWindow.fill(white)
                text_screen("Game Over! Press Enter To Continue", red, 100, 250)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameloop()

            else:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_UP:
                            velocity_y = - init_velocity
                            velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0

                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                    score +=1
                    food_x = random.randint(20, screen_width - 30)
                    food_y = random.randint(60, screen_height - 30)
                    snk_length +=5

                gameWindow.fill(white)
                text_screen("Score: " + str(score * 10), red, 5, 5)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
                pygame.draw.line(gameWindow, red, (0,40), (900,40),5)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list)>snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_over = True

                if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                    game_over = True
                plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()

    gameloop()
    return

#The main loop to take in commands and do respective operations.
    
if __name__ == '__main__':
    while True:
        command = take_commands()
        if "bye" in command:
            speak("Sure, sir! As you wish. Have a good day!")
            break
        if "time" in command:
            import datetime
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)
        if "date" in command:
            import datetime
            current_date = datetime.date.today().strftime("%B %d, %Y")
            speak("Today's date is " + current_date)
        if "weather" in command:
            speak("Please tell me the city name.")
            city_name = take_commands()
            weather = get_weather(city_name)
            if weather:
                temperature = weather["temperature"]
                description = weather["description"]
                humidity = weather["humidity"]
                weather_info = f"The weather in {city_name} is {description}. The temperature is {temperature} degrees Celsius. The humidity is {humidity} percent."
                speak(weather_info)
            else:
                speak("Sorry, I couldn't retrieve the weather information.")
        if "joke" in command:
            joke = get_random_joke()
            if joke:
                speak(joke)
            else:
                speak("Sorry, I couldn't fetch a joke at the moment.")
        if "riddle" in command:
            riddle = get_random_riddle()
            if riddle:
                speak("Here's a riddle for you:")
                speak(riddle)
            else:
                speak("Sorry, I couldn't fetch a riddle at the moment.")
        if "define" in command:
                speak("Please tell me the word you want to define.")
                word = take_commands()
                definition = get_dictionary_definition(word)
                if definition:
                    speak(f"The definition of '{word}' is:")
                    speak(definition)
                else:
                    speak("Sorry, I couldn't find a definition for the word.")
        if "speech" in command:
            speak("Please start speaking.")
            text = convert_speech_to_text()
            if text:
                speak("You said: " + text)
                print("You said: " + text)
            else:
                speak("Sorry, I couldn't convert your speech to text.")
        
        if "translate" in command:
            speak("Please enter the text you want to translate.")
            text = input("Text: ")
            speak("Please enter the target language.")
            target_language = input("Target Language: ")
            translated_text = translate_text(text, target_language)
            if translated_text:
                speak(f"The translated text is: {translated_text}")
                print(f"The translated text is: {translated_text}")
            else:
                speak("Sorry, the translation failed.")
        
        if "go to sleep" in command:
            speak("Going to sleep mode.")
            mute_sound()
            enable_airplane_mode()  
        if "calculate" in command:
            expression = input("Enter the expression to calculate: ")
            result = calculate_expression(expression)
            if result:
                print(f"Result: {result}")
                speak(f'The result is: {result}')

        if "password" in command:
            speak("Please enter the number of characters for the password.")
            length = int(input("Enter the number of characters: "))
            password = generate_password(length)
            speak("Generated Password: ")
            print(password)

        if "game" in command:
            speak("Opening Snake Game!")
            play_snake_game()
        continue_listening = True