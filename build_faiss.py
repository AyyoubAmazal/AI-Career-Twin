import numpy as np
import faiss
import os

STORE_DIR = "career_twin_store"

def build_index():
    embeddings = np.load(f"{STORE_DIR}/embeddings.npy").astype("float32")
    dim = embeddings.shape[1]

    print("Building FAISS CPU index (Windows)...")

    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    faiss.write_index(index, f"{STORE_DIR}/faiss.index")
    print("FAISS index created with", index.ntotal, "vectors")


if __name__ == "__main__":
    build_index()
