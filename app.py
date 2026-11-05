from retrieval import Retriever
from rag_engine import RAGEngine
from prompt import PROMPT
from roadmap_memory import RoadmapMemory
import json

retriever = Retriever()
rag = RAGEngine()
memory = RoadmapMemory()

def run_careertwin(user_profile):
    # STEP 1 — Check memory first
    cached = memory.search_similar(user_profile)
    if cached:
        print("Using cached roadmap 🔥")
        return {"roadmap": cached, "cached": True}

    # STEP 2 — If not cached: run full pipeline
    top5 = retriever.search(user_profile)
    roadmap = rag.generate(user_profile, top5, PROMPT)

    # STEP 3 — Save roadmap for future reuse
    memory.store(user_profile, roadmap)

    return {"roadmap": roadmap, "cached": False}



