import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

STORE_DIR = "career_twin_store"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"

class Retriever:

    def __init__(self):
        self.index = faiss.read_index(f"{STORE_DIR}/faiss.index")
        self.meta = json.load(open(f"{STORE_DIR}/chunks_meta.json", "r", encoding="utf-8"))
        self.model = SentenceTransformer(MODEL)

    def embed_user(self, user_input):
        query = {
            "skills": user_input.get("skills", []),
            "experience": user_input.get("experience", ""),
            "education": user_input.get("education", ""),
            "languages": user_input.get("languages", []),
            "certifications": user_input.get("certifications", []),
            "goal": user_input.get("goals", "")
        }

        text = json.dumps(query)
        emb = self.model.encode(text, normalize_embeddings=True)
        return np.array([emb]).astype("float32")

    def search(self, user_input, k=5):
        vec = self.embed_user(user_input)
        scores, ids = self.index.search(vec, 5)

        results = []
        for sc, idx in zip(scores[0], ids[0]):
            m = self.meta[idx]
            results.append({
                "name": m["name"],
                "url": m["url"],
                "about": m["about"],
                "chunk": m["chunk"],
                "score": float(sc)
            })

        return results
