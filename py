# sentiment_analyzer.py

# Install dependencies first:
# pip install textblob

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😀"
    elif polarity < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    print(" Simple Sentiment Analyzer ")
    while True:
        user_input = input("Enter a sentence (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print("Sentiment:", analyze_sentiment(user_input))
