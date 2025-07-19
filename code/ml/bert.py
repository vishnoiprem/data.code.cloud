import torch
from transformers import BertTokenizer, BertModel  # From Hugging Face
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 2: Load pretrained model (bert-base-uncased for uncased text)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()  # Set to evaluation mode

# Step 3: Preprocess data (tokenize sentences with padding/truncation)
sentences = ["The king rules wisely.", "The queen is royal.", "I ate an apple."]
inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')  # Returns tensors ready for model

# Step 4: Generate embeddings (use [CLS] token for contextual sentence vectors)
with torch.no_grad():  # No gradients for inference
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :].numpy()  # [CLS] token from first position

print("Embedding shape for first sentence:", embeddings[0].shape)  # E.g., (768,) – deep contextual vector

# Step 5: Semantic search (find similar to query "A wise ruler")
query = "A wise ruler"
query_input = tokenizer(query, return_tensors='pt')
with torch.no_grad():
    query_output = model(**query_input)
    query_emb = query_output.last_hidden_state[:, 0, :].numpy()
similarities = cosine_similarity(query_emb, embeddings)
print("Similarities to query:", similarities)  # E.g., high for "king" sentence due to context
top_match = sentences[np.argmax(similarities[0])]
print("Top matching sentence:", top_match)
