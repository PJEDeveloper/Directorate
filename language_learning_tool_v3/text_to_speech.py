import pyttsx3

# Function to implement text-to-speech capabilities
def speak(text):
    # Establish text-to-speech engine
    engine = pyttsx3.init()
    # Get available voices and select a second voice (female)
    voices = engine.getProperty('voices')
    # Attempt to select a female voice by setting a specific index of 1
    try:
        # Set voice property to 1 for female
        engine.setProperty('voice', voices[1].id)
    except IndexError:
        print('Female voice not found...using default voice...')
    # Pass text to say method
    engine.say(text)
    # Call run and Wait method on text-to-speech object
    engine.runAndWait()

