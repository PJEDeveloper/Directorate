'''
PDF Sentiment Analysis Program

Description:
This program provides a graphical user interface (GUI) for performing sentiment analysis on text extracted from PDF
files. It utilizes the pdfplumber library to extract text from the first page of a selected PDF document and
then analyzes the sentiment of that text using the Natural Language Toolkit (NLTK) with its VADER Sentiment Intensity
Analyzer.

Functionality:
- Load a PDF file through a file dialog.
- Display the name of the loaded PDF file within the GUI.
- Extract text from the first page of the loaded PDF.
- Analyze the extracted text to determine if the sentiment is Positive or Negative.
- Display the sentiment analysis result and detailed sentiment scores in the GUI.

Usage:
1. Run the program. The GUI will open with a button labeled 'Load PDF'.
2. Click 'Load PDF' to open a file dialog. Choose a PDF file to load.
3. If text is successfully extracted from the PDF, the 'Analyze Sentiment' button will become active.
4. Click 'Analyze Sentiment' to perform sentiment analysis on the extracted text.
5. View the sentiment result and scores displayed below in the GUI.

Dependencies:
- Python 3.x
- tkinter for the GUI.
- nltk for sentiment analysis (ensure the VADER lexicon is downloaded).
- pdfplumber for reading PDF files.

Ensure you have the necessary libraries installed:
pip install nltk
pip install pdfplumber
python -m nltk.downloader vader_lexicon

Note:
- The program currently only processes text from the first page of the PDF.
- Ensure that the PDF contains selectable text and not images of text for accurate extraction and analysis.

Patrick Hill
April 13, 2024
MS548 - Advanced Programming Concepts and AI
'''

import tkinter as tk
from tkinter import filedialog, scrolledtext
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pdfplumber
nltk.download('vader_lexicon')

# Function to open and read ABC News PDF about Biden press release
def load_pdf():
    global pdf_name_label, text_display, analyze_button  # Ensure that the function recognizes these variables (scope)
    handle = filedialog.askopenfilename(filetypes=[("PDF Files", '*.pdf')])
    if handle:
        pdf_file_name = handle.split('/')[-1]  # Extracts the file name from the full path
        pdf_name_label.config(text=f'Loaded PDF: {pdf_file_name}')  # Display the PDF file in the GUI
        with pdfplumber.open(handle) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            if text:
               text_display.config(state=tk.NORMAL)
               text_display.delete('1.0', tk.END)
               text_display.insert(tk.END, text)
               text_display.config(state=tk.DISABLED)
               analyze_button.config(state=tk.NORMAL)
            else:
                text_display.config(state=tk.NORMAL)
                text_display.delete('1.0', tk.END)
                text_display.insert(tk.END, text='Failed to extract text or text is empty.')
                text_display.config(state=tk.DISABLED)
                analyze_button.config(state=tk.DISABLED)
            print('PDF loaded successfully.')
    else:
        print('No PDF file selected.')
        pdf_name_label.config(text='No PDF loaded')
        text_display.config(state=tk.NORMAL)
        text_display.delete('1.0', tk.END)
        text_display.config(state=tk.DISABLED)

# Function to perform sentiment analysis
def analyze_sentiment():
    global text_label, result_label  # Ensure that the function recognizes these variables due to being outside scope
    text = text_display.get('1.0', tk.END)
    if text.strip():
        try:
            sia = SentimentIntensityAnalyzer()
            sentiment = sia.polarity_scores(text)
            result = 'Positive' if sentiment['compound'] >= 0 else 'Negative'
            result_label.config(text=f'Sentiment: {result}\nScores: {sentiment}')
        except Exception as e:
            result_label.config(text='Error in analyzing sentiment.')
            print(f'Error: {e}')
        print('Sentiment Analysis completed.')
    else:
        print('No text available to analyze.')

# Create the GUI
root = tk.Tk()
root.title('PDF Sentiment Analysis')

# Button to load the PDF
load_button = tk.Button(root, text='Load PDF', command=load_pdf)
load_button.pack(pady=20)

# Label to display the loaded PDF file name
pdf_name_label = tk.Label(root, text='No PDF loaded.')
pdf_name_label.pack(pady=5)

# Scrollable text display
text_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)
text_display.pack(pady=10)

# Display Results
result_label = tk.Label(root, text='', wraplength=300)
result_label.pack(pady=10)

# Button to analyze sentiment (initially disabled)
analyze_button = tk.Button(root, text='Analyze Sentiment', state=tk.DISABLED, command=analyze_sentiment)
analyze_button.pack(pady=20)

# Start the GUI
root.mainloop()
