
# Voice Assistant

This is a Voice Assistant program written in Python that uses speech recognition, text-to-speech conversion, and various APIs to perform tasks such as getting weather information, telling jokes, solving riddles, defining words, translating text, playing games, and more.

## Installation

1. Clone the repository:
   ```shell
   git clone <repository_url>
   ```

2. Install the required dependencies:
   ```shell
   pip install pyttsx3
   pip install SpeechRecognition
   pip install requests
   pip install pygame
   ```

3. Obtain API keys:
   - OpenWeatherMap API key: Sign up and get the API key from [OpenWeatherMap](https://openweathermap.org/) to retrieve weather information.
   - Joke API key: Get the API key from [JokeAPI](https://jokeapi.dev/) to fetch random jokes.
   - Shazam API key: Obtain the API key from [RapidAPI](https://rapidapi.com/) to use the Shazam API.
   - RapidAPI key: Sign up on [RapidAPI](https://rapidapi.com/) to access the Urban Dictionary API.

4. Update the API keys in the code:
   - Replace `API_KEY` with your OpenWeatherMap API key.
   - Replace `shazam_key` with your Shazam API key.
   - Update the RapidAPI key in the `headers` dictionary for the Urban Dictionary API.

## Usage

1. Run the program:
   ```shell
   python voice_assistant.py
   ```

2. Follow the voice prompts and provide voice commands to interact with the voice assistant.

## Features

- Get the current time and date.
- Retrieve weather information for a specific city.
- Fetch random jokes.
- Solve random riddles.
- Define words using the Urban Dictionary API.
- Convert speech to text.
- Translate text to different languages using the Google Translate API.
- Mute laptop sound and enable airplane mode.
- Calculate mathematical expressions using the Big Numbers Calculation API.
- Generate random passwords.
- Play the classic Snake game.

## Contributing

Contributions to improve the functionality or add new features to this Voice Assistant are welcome! Please feel free to create issues or submit pull requests.

Please note that the API keys mentioned in the code should be obtained by following the instructions provided for each API service. Also, ensure that you have the necessary dependencies installed before running the program.
