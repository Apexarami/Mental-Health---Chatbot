import random
import json
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset from the correct path
DATASET_PATH = r"C:\Users\apexa\PycharmProjects\mental health\chatbot_dataset.json"

with open(DATASET_PATH, "r", encoding="utf-8") as file:
    data = json.load(file)

# Preprocess patterns for TF-IDF vectorization
patterns = []
responses = {}

# Extract patterns and responses from dataset
for intent in data["intents"]:
    for pattern in intent.get("patterns", []):  # Use .get() to avoid KeyError if "patterns" is missing
        patterns.append(pattern)
        # Check if "responses" key exists before accessing it
        if "responses" in intent:
            responses[pattern] = intent["responses"]
        else:
            responses[pattern] = ["Sorry, I don't have an answer for that."]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on all patterns
vectorizer.fit(patterns)


@app.route("/")
def home():
    return render_template("index.html")  # Serves the chatbot frontend


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Vectorize the user input and calculate similarity with patterns
    user_vector = vectorizer.transform([user_message])
    pattern_vectors = vectorizer.transform(patterns)

    similarities = cosine_similarity(user_vector, pattern_vectors)

    # Get the index of the most similar pattern
    best_match_idx = np.argmax(similarities)

    # Get the corresponding response for the best matching pattern
    matched_pattern = patterns[best_match_idx]
    response = random.choice(responses[matched_pattern])

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
