
Webpage Sentiment Analysis Program

Description:
This program analyzes the sentiment of text extracted from web pages. It provides a graphical user interface (GUI) built 
using Tkinter. Users can input a URL, and the program will fetch the page content, extract text from it using
BeautifulSoup, and then use the NLTK library with its VADER Sentiment Intensity Analyzer to assess the sentiment.

Functionality:
- Load and display the text of a webpage from a provided URL.
- Analyze and display the sentiment of the extracted text, indicating whether the overall sentiment is Positive or Negative.
- Display detailed sentiment scores showing the neutrality, positivity, and negativity of the text.

Usage:
1. Start the program; the GUI will open.
2. Click the "Load URL" button to enter a URL of a webpage.
3. If the webpage is accessible and text can be extracted, the "Analyze Sentiment" button will be enabled.
4. Click "Analyze Sentiment" to see the sentiment analysis results.

Dependencies:
- Python 3
- tkinter (for the GUI)
- nltk (for sentiment analysis)
- requests (for fetching webpages)
- BeautifulSoup4 (for parsing HTML content)
- VADER lexicon (included with NLTK)

Installation of Dependencies:
Ensure you have Python installed, then run these commands:
pip install nltk
pip install requests
pip install beautifulsoup4
python -m nltk.downloader vader_lexicon

Author: Patrick Hill
Date Created: 4/13/2024

Notes:
- The program attempts to extract text only from paragraph tags of the HTML content.
- Ensure the URL starts with 'http://' or 'https://' or it will be automatically prepended with 'http://'.
- Error handling is in place for network issues or poorly formatted HTML that could hinder text extraction.
