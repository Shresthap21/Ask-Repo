import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings_list = []
documents = []
metadata = []

index = None


def get_embedding(text):
    return model.encode(text)


def store_chunks(chunks):

    global index

    for chunk in chunks:

        embedding = get_embedding(chunk["content"])

        embeddings_list.append(embedding)
        documents.append(chunk["content"])
        metadata.append(chunk["file"])

    vectors = np.array(embeddings_list).astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    print("Stored", len(vectors), "vectors in FAISS index")


def search(query, top_k=3):

    if index is None:
        raise ValueError("Vector index is empty. Please index the repository first.")

    query_embedding = model.encode(query)

    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []

    for i in indices[0]:
        results.append({
            "file": metadata[i],
            "content": documents[i]
        })

    return results