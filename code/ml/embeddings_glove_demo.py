# Quick check for problematic file name (optional safety net)
import os
import sys

current_file = os.path.basename(sys.argv[0])
if current_file.lower().startswith('gensim'):
    print("Warning: File name might shadow Gensim module—rename to avoid import errors!")
    # Continue anyway, but fix for real runs

# Step 1: Import libraries
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 2: Load pretrained model (download glove.6B.50d.txt from Stanford and update path)
model_path = 'glove.6B.50d.txt'  # Replace with your file path
model = KeyedVectors.load_word2vec_format(model_path, binary=False, no_header=True)  # Load GloVe format

# Step 3: Preprocess data (just a list of words—no heavy prep needed)
words = ["king", "queen", "apple"]

# Step 4: Generate embeddings (extract vectors from the model)
embeddings = np.array([model[word] for word in words])  # Stack into array
print("Embedding for 'king':", model["king"])  # Peek at one vector (50 dims)

# Step 5: Semantic search (find similar to "king")
query = model["king"].reshape(1, -1)  # Reshape for similarity
similarities = cosine_similarity(query, embeddings)
print("Similarities to 'king':", similarities)  # E.g., high for "queen", low for "apple"
top_match = words[np.argmax(similarities[0])]
print("Top similar word:", top_match)
