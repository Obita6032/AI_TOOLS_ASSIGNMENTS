import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample Amazon review
review = "I love the Apple iPhone 13. The camera quality is amazing and it beats Samsung easily!"

# Apply spaCy pipeline
doc = nlp(review)

# Extract named entities
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")

# Rule-based sentiment
positive_words = ['love', 'amazing', 'great', 'beats']
negative_words = ['bad', 'worst', 'poor', 'hate']

sentiment_score = 0
for token in doc:
    if token.text.lower() in positive_words:
        sentiment_score += 1
    elif token.text.lower() in negative_words:
        sentiment_score -= 1

sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
print(f"Sentiment: {sentiment}")
