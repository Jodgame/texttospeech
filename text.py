from gtts import gTTS
import os
import time

while True:
    # Clear the screen
    os.system('clear')  # For Linux/Mac
    # os.system('cls')  # For Windows

    # Define the input message in red color
    message = '\033[91m' + 'Please enter the text you want to play or type "exit" to quit: ' + '\033[0m'

    # Define the number of times to blink
    blink_count = 0

    # Loop to blink the message
    for _ in range(blink_count):
        print(message, end='\r')  # Print message without newline
        time.sleep(0.5)  # Wait for half a second
        print(' ' * len(message), end='\r')  # Clear the message
        time.sleep(0.5)  # Wait for half a second

    # Get user input
    mytext = input(message)

    if mytext.lower() == 'exit':
        break

    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")

    # Play the audio
    os.system("play welcome.mp3")
