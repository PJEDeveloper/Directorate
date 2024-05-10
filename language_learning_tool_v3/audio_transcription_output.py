import speech_recognition as sr
import text_to_speech as tts
import language_processing as lp
import tkinter as tk
from tkinter import scrolledtext
import threading

# Global variables
# Instantiate speech recognizer
recognizer = sr.Recognizer()
# Bool flag marking recording state
is_recording = False

# Function to help user differentiate polarity and subjectivity meanings
# passed by lp module
def interpret_sentiment(polarity, subjectivity):
    # Flow control to determine polarity output
    if polarity > 0.5:
        sentiment = 'Very Positive'
    elif polarity > 0:
        sentiment = 'Positive'
    elif polarity == 0:
        sentiment = 'Neutral'
    elif polarity < -0.5:
        sentiment = 'Very Negative'
    else:
        sentiment = 'Negative'

    # Flow control to determine output for subjectivity
    if subjectivity > 0.7:
        subjectivity_description = 'Highly Subjective'
    elif subjectivity > 0.3:
        subjectivity_description = 'Somewhat Subjective'
    else:
        subjectivity_description = 'Fairly Objective'

    # Return a meaningful description for the user
    return sentiment, subjectivity_description

# Function to initiate GUI
def init_gui(root):
    # Global variables for descriptors/attributes
    global transcript_label, transcript_box, start_button, stop_button

    # Function to start the recording
    # set is_recording to True, update GUI, and start new thread for
    # audio recording
    def start_recording():
        global is_recording
        is_recording = True
        transcript_label.config(text="Recording...")
        stop_button['state'] = 'normal'
        start_button['state'] = 'disabled'
        threading.Thread(target=record_audio).start()

    # Function to stop the recording
    # set is_recording to False disabling further recording
    def stop_recording():
        global is_recording
        is_recording = False
        stop_button['state'] = 'disabled'

    # Function to record audio
    def record_audio():
        global is_recording
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            # Keep recording while True
            while is_recording:
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    # After recoding stops, process captured audio
                    process_audio(audio)
                except sr.WaitTimeoutError:
                    continue # If timeout occurred, record again

    # Function to process audio recording
    def process_audio(audio):
        try:
            # Convert recorded audio to text
            text = recognizer.recognize_google(audio)
            # Enable transcript box
            transcript_box.config(state='normal')
            # Clear the contents of the transcript box
            transcript_box.delete(1.0, tk.END)
            # Insert converted text into transcript box
            transcript_box.insert(tk.END, text)
            # Make transcript box read-only access
            transcript_box.config(state='disabled')
            # Perform sentiment analysis on text
            polarity, subjectivity = lp.analyze_sentence(text)
            # Interpret and assign polarity and subjectivity
            sentiment, subjectivity_description = interpret_sentiment(polarity, subjectivity)
            # Speak results of converted text
            tts.speak(f'This is considered {sentiment} and {subjectivity_description}')
            # Update GUI label with polarity and subjectivity
            transcript_label.config(text=f'Sentiment: {sentiment} Subjectivity: {subjectivity_description}')
        except sr.RequestError:
            # Handle API errors
            transcript_label.config(text='API unavailable, please try again')
        except sr.UnknownValueError:
            # Handle unrecognized speech
            transcript_label.config(text='Unable to recognize speech, please try again')
        finally:
            # Allow for re-recording
            start_button['state'] = 'normal'

    # Instantiate instance of transcription label set to Start Recording
    transcript_label = tk.Label(root, text="Press 'Start Recording' to begin")
    # Add label
    transcript_label.pack()

    # Instantiate instance of transcription box to display text set to non-editable
    transcript_box = scrolledtext.ScrolledText(root, state='disabled', height=10)
    # Add box
    transcript_box.pack()

    # Instantiate instance of start button set to start recording function
    start_button = tk.Button(root, text='Start Recording', command=start_recording)
    # Add start button
    start_button.pack()

    # Instantiate instance of stop button set to stop recording function
    stop_button = tk.Button(root, text='Stop Recording', command=stop_recording, state='disabled')
    # Add stop button
    stop_button.pack()







