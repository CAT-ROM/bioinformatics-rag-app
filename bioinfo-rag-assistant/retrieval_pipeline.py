import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load model (use the same one used to create embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load stored embeddings and documents
with open('embeddings/text_embeddings.pkl', 'rb') as f:
    data = pickle.load(f)
    doc_embeddings = data['embeddings']  # shape: (N, D)
    documents = data['documents']        # list of original texts

# Create FAISS index
embedding_dim = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(embedding_dim)
index.add(doc_embeddings)

def embed_query(query: str) -> np.ndarray:
    """
    Converts a query string into an embedding vector.
    """
    return model.encode([query])[0].reshape(1, -1)

def retrieve_documents(query: str, k: int = 3) -> list:
    """
    Retrieves top-k most similar documents to the query.
    """
    query_vector = embed_query(query)
    distances, indices = index.search(query_vector, k)
    return [documents[i] for i in indices[0]]
