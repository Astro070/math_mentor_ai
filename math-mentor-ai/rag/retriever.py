# retriever.py

import os  # used for file operations
import numpy as np  # numeric operations
import faiss  # vector search library
from sentence_transformers import SentenceTransformer  # embedding model

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight embedding model

documents = []  # list to store knowledge documents

# Read all text files from the data folder
data_folder = "data"

for file in os.listdir(data_folder):  # loop through files
    if file.endswith(".txt"):  # only read txt files
        with open(os.path.join(data_folder, file), "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(text)  # store document

# Convert documents to embeddings
doc_embeddings = model.encode(documents)

# Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
index.add(np.array(doc_embeddings))


# retriever.py

def retrieve_context(query):

    # Example retrieved document
    context = "The derivative rule d/dx (x^n) = n*x^(n-1)"

    source = "calculus_rules.txt"

    return {
        "context": context,
        "source": source
    }