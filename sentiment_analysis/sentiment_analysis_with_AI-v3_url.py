'''
Webpage Sentiment Analysis Program

Description:
This Python program provides a graphical user interface (GUI) for analyzing the sentiment of text extracted from web
pages. It uses the `requests` library to fetch the content of a specified URL and `BeautifulSoup` from bs4 to parse
the HTML content and extract text. The sentiment of the extracted text is analyzed using the Natural Language
Toolkit (NLTK) with its VADER Sentiment Intensity Analyzer, which assesses whether the sentiment of the text is
positive or negative.

Functionality:
- Allow the user to enter a URL from which text will be fetched.
- Display the loaded URL and any status messages in the GUI.
- Extract text from the webpage, specifically from paragraph tags.
- Analyze the sentiment of the extracted text and display whether it is Positive or Negative.
- Show detailed sentiment scores which include proportions of positivity, negativity, and neutrality.

Usage:
1. Run the program; the GUI titled 'Webpage Sentiment Analysis' will open.
2. Click the 'Load URL' button and enter a URL when prompted.
3. After the URL is processed, if text is successfully extracted, the 'Analyze Sentiment' button will become active.
4. Click 'Analyze Sentiment' to display the sentiment analysis results in the GUI.

Dependencies:
- Python 3.x
- tkinter for the GUI.
- requests for fetching web pages.
- BeautifulSoup4 for parsing HTML.
- nltk for sentiment analysis, including the VADER lexicon.

Installation of Dependencies:
Ensure Python is installed and run these commands:
pip install requests
pip install beautifulsoup4
pip install nltk
python -m nltk.downloader vader_lexicon

Notes:
- The program currently only extracts and analyzes text from paragraph (p) tags of the HTML.
- The URL should start with 'http://' or 'https://'; otherwise, 'http://' will be prepended automatically.
- Ensure robust internet connectivity for fetching web pages without interruptions.

Patrick Hill
April 13, 2024
MS548 - Advanced Programming Concepts and AI
'''

import tkinter as tk
from tkinter import simpledialog, scrolledtext
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup

nltk.download('vader_lexicon')

# Function to open and read ABC News PDF about Biden press release
def load_webpage():
    global page_content_label, text_display, analyze_button  # Ensure that the function recognizes these variables (scope)
    url = simpledialog.askstring('Input', 'Please enter the URL:', parent=root)
    if url:
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url  # Prepend 'http://' if no scheme is specified
        page_content_label.config(text=f'URL Loaded: {url}')  # Display the loaded URL in GUI
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract text from the webpage
            text = ' '.join(p.get_text() for p in soup.find_all('p'))  # Extract paragraphs only
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
            print('Webpage loaded successfully.')
        except Exception as e:
            print(f'Error loading webpage: {e}')
            page_content_label.config(text='Error loading webpage.')
            text_display.config(state=tk.NORMAL)
            text_display.delete('1.0', tk.END)
            text_display.config(state=tk.DISABLED)

# Function to perform sentiment analysis
def analyze_sentiment():
    global text_display, result_label  # Ensure that the function recognizes these variables due to being outside scope
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
root.title('Webpage Sentiment Analysis')

# Button to load the PDF
load_button = tk.Button(root, text='Load URL', command=load_webpage)
load_button.pack(pady=20)

# Label to display the loaded PDF file name
page_content_label = tk.Label(root, text='No URL loaded.')
page_content_label.pack(pady=5)

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
