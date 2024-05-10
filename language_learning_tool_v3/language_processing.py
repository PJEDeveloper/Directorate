from textblob import TextBlob


# Function to analyze language processing
def analyze_sentence(sentence):
    # Create a Textblob object passing sentence argument
    blob = TextBlob(sentence)

    # Perform sentiment analysis with sentiment property called on blob object
    sentiment = blob.sentiment

    # Return the polarity and subjectivity attributes of the sentiment object
    return sentiment.polarity, sentiment.subjectivity
