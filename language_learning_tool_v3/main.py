# =====================================================================
# Title: Assignment - Library Implementations
# Description: This language learning tool that uses speech recognition and speech-to-text combined
# with sentiment analysis from TextBlob to give the user feed back about polarity and subjectivity of
# recorded audio. The recording of audio is interfaced with Tkinter GUIs to allow the user to start and
# stop recording capabilities with outputs both in GUI based text and audio formats.
# Author: Patrick Hill
# Estimated Development Time: 8 hours
# Created Date: March 24, 2024
# Research and Design 1000-1200 March 24, 2024
# language_learning_tool March 24, 2024, 1300-1400: First iteration of program had main.py,
# speech_recognition_handler.py, text_to_speech.py, and language_processing.py modules with
# recording prompt input through command line.
# language_learning_tool_v2 March 24, 2024, 1500-1700: Second iteration of program added audio_transcription_output.py
# to remove command line input and add GUI user interfacing for recording and output.
# language_learning_tool_v2 March 25, 2024 2100-2130: Removed speech_recognition_handler.py module, moving appropriate
# functions inside audio_transcription_output.py functions. Streamlining code improved return time of
# audio transcription.
# Total Development Time: 5.5 hours
# Due to being unfamiliar with the libraries used in the program, I allotted plenty of time of R&D. I believe more time
# spent on the front-end with R&D is leading to less time in development with better end products. For example, like
# the last project, this too had three iterations, and each built on the functions of the last making it better than
# before. Also, encapsulating code in modules and only calling it when necessary lead to best practices at runtime
# and less overall development time. This is something I will continue to use in future projects and definitely
# see the value in just such an approach.

import tkinter as tk
import audio_transcription_output as ato


def main():

    # Set up the tkinter GUI
    # Initialize main root window
    root = tk.Tk()
    # Set title
    root.title('Speech Recognition')

    # Initiate the GUI Interface through ato function call
    ato.init_gui(root)

    # Start Tkinter event loop
    root.mainloop()

# Call the main function
if __name__ == '__main__':
    main()