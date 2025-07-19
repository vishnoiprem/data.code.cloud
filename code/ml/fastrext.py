# Step 1: Import libraries
from gensim.models import FastText
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 2: Preprocess data (list of sentences as word lists)
sentences = [
    ["he", "is", "the", "king"],  # Samples to train on
    ["the", "king", "is", "royal"],
    ["she", "is", "the", "royal", "queen"],
    ["i", "like", "apple", "pie", "for", "dessert"],
    ["i", "dont", "drive", "fast", "cars"]
]

# Step 3: Load/Train model (train a small FastText—uses subwords!)
model = FastText(sentences, vector_size=50, window=2, min_count=1, workers=4, min_n=3, max_n=6)  # n-grams from 3-6 chars

# Step 4: Generate embeddings (get vectors for words—even unseen ones!)
words = ["king", "queen", "apple", "unhappiness"]  # "unhappiness" isn't in training, but subwords handle it!
embeddings = np.array([model.wv[word] for word in words])  # Stack into array
print("Embedding for 'unhappiness' (via subwords):", model.wv["unhappiness"])  # It works thanks to n-grams!

# Step 5: Semantic search (find similar to "king")
query = model.wv["king"].reshape(1, -1)  # Reshape for similarity
similarities = cosine_similarity(query, embeddings)
print("Similarities to 'king':", similarities)  # E.g., high for "queen", maybe some link to "unhappiness" via subwords
top_match = words[np.argmax(similarities[0])]
print("Top similar word:", top_match)
