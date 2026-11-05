import json
import numpy as np
from sentence_transformers import SentenceTransformer
import os

STORE_DIR = "career_twin_store"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def generate_embeddings():
    chunks = json.load(open(f"{STORE_DIR}/semantic_chunks.json", "r", encoding="utf-8"))

    model = SentenceTransformer(MODEL, device="cuda")  # GPU

    embeddings = [model.encode(c["chunk"], normalize_embeddings=True) for c in chunks]

    np.save(f"{STORE_DIR}/embeddings.npy", np.array(embeddings))
    json.dump(chunks, open(f"{STORE_DIR}/chunks_meta.json", "w", encoding="utf-8"), indent=2)

    print("GPU embeddings generated!")


if __name__ == "__main__":
    generate_embeddings()
