import faiss
import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer

CACHE_DIR = "roadmap_cache"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

class RoadmapMemory:

    def __init__(self):
        self.model = SentenceTransformer(EMBED_MODEL)

        os.makedirs(CACHE_DIR, exist_ok=True)

        self.meta_file = os.path.join(CACHE_DIR, "meta.json")
        self.index_file = os.path.join(CACHE_DIR, "faiss.index")

        # load metadata
        self.meta = []
        if os.path.exists(self.meta_file):
            self.meta = json.load(open(self.meta_file, "r", encoding="utf-8"))

        # load FAISS
        self.dim = 384
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
        else:
            self.index = faiss.IndexFlatIP(self.dim)

    def embed_profile(self, profile_dict):
        text = json.dumps(profile_dict, indent=2)
        emb = self.model.encode(text, normalize_embeddings=True)
        return emb.astype("float32")

    def search_similar(self, user_profile, threshold=0.88):
        if len(self.meta) == 0:
            return None

        emb = self.embed_profile(user_profile).reshape(1, -1)
        scores, ids = self.index.search(emb, 1)

        if scores[0][0] >= threshold:
            return self.meta[int(ids[0][0])]["roadmap"]
        return None

    def store(self, user_profile, roadmap):
        emb = self.embed_profile(user_profile)

        self.index.add(np.array([emb]))
        self.meta.append({
            "user_profile": user_profile,
            "roadmap": roadmap
        })

        faiss.write_index(self.index, self.index_file)
        json.dump(self.meta, open(self.meta_file, "w", encoding="utf-8"), indent=2)
