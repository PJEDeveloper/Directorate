
PDF Sentiment Analysis Program

Description:
This program is designed to analyze the sentiment of text extracted from PDF files. It uses a graphical user interface
(GUI) built with Tkinter, reads PDF files using the pdfplumber library, and performs sentiment analysis using the
Natural Language Toolkit (NLTK) with its VADER Sentiment Intensity Analyzer.

Functionality:
- Load and display PDF files selected by the user.
- Extract text from the first page of the PDF.
- Analyze and display the sentiment of the extracted text as either Positive or Negative.
- Display sentiment scores detailing the neutrality, positivity, and negativity of the text.

Usage:
1. Start the program. The GUI will open.
2. Click the "Load PDF" button to open a file dialog and select a PDF file.
3. Once a file is loaded, if the text can be extracted, the "Analyze Sentiment" button will be enabled.
4. Click "Analyze Sentiment" to display the sentiment analysis results.

Dependencies:
- Python 3
- tkinter (for the GUI)
- nltk (for sentiment analysis)
- pdfplumber (for reading PDF files)
- VADER lexicon (included with NLTK)

Installation of Dependencies:
Ensure you have Python installed, then run these commands:
pip install nltk
pip install pdfplumber
python -m nltk.downloader vader_lexicon

Author: Patrick Hill
Date Created: 4/13/2024

Notes:
- The program currently only reads from the first page of the PDF.
- Ensure that the PDF contains selectable text and is not just image-based.
