# retriever.py

import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
sources = []

data_folder = "data"

# Check if data folder exists
if os.path.exists(data_folder):

    for file in os.listdir(data_folder):

        if file.endswith(".txt"):

            file_path = os.path.join(data_folder, file)

            with open(file_path, "r", encoding="utf-8") as f:

                text = f.read()

                documents.append(text)
                sources.append(file)

else:
    print("WARNING: data folder not found")


# If documents exist → create FAISS index
if len(documents) > 0:

    doc_embeddings = model.encode(documents)

    dimension = doc_embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(doc_embeddings))

else:

    index = None


# Retrieval function
def retrieve_context(query):

    # If no documents available
    if index is None:
        return {
            "context": "No knowledge documents found.",
            "source": "none"
        }

    query_embedding = model.encode([query])

    D, I = index.search(np.array(query_embedding), k=1)

    doc_index = I[0][0]

    return {
        "context": documents[doc_index],
        "source": sources[doc_index]
    }
