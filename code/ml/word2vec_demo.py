# Step 1: Import libraries
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 2: Preprocess data (list of sentences as word lists)
sentences = [
    ["he", "is", "the", "king"],  # Sample from towardsdatascience.com
    ["the", "king", "is", "royal"],
    ["she", "is", "the", "royal", "queen"],
    ["i", "like", "apple", "pie", "for", "dessert"],  # From builtin.com
    ["i", "dont", "drive", "fast", "cars"]
]

# Step 3: Load/Train model (train a small Word2Vec on our data)
model = Word2Vec(sentences, vector_size=50, window=2, min_count=1, workers=4)  # Small size for demo

# Step 4: Generate embeddings (get vectors for words)
words = ["king", "queen", "apple"]
embeddings = np.array([model.wv[word] for word in words])  # Stack into array
print("Embedding for 'king':", model.wv["king"])  # Peek at one vector

# Step 5: Semantic search (find similar to "king")
query = model.wv["king"].reshape(1, -1)  # Reshape for similarity
similarities = cosine_similarity(query, embeddings)
print("Similarities to 'king':", similarities)  # E.g., high for "queen", low for "apple"
top_match = words[np.argmax(similarities[0])]
print("Top similar word:", top_match)
