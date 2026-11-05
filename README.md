# 🎯 CareerTwin AI – Personalized Career Roadmap Generator

An AI-powered career assistant that analyzes user profiles, retrieves similar professional profiles using semantic search, and generates personalized career roadmaps with the help of Large Language Models (LLMs).

CareerTwin AI helps users identify career opportunities, discover missing skills, and build a structured learning and professional development plan based on real-world career profiles.

## 🚀 Key Features

- **👤 Profile Analysis:** Analyze skills, experience, education, languages, certifications, and career goals.
- **🔍 Semantic Search:** Retrieve the 5 most relevant professional profiles using FAISS similarity search.
- **🤖 AI-Powered Recommendations:** Generate personalized career roadmaps using GPT-OSS-20B through Ollama.
- **🏆 Best Profile Matching:** Identify the single most relevant professional profile as inspiration for the user's career path.
- **🗺️ Career Roadmap Generation:** Create structured short-term, mid-term, and long-term development plans.
- **🧠 Roadmap Memory:** Store previous roadmaps and reuse them when similar user profiles are submitted.
- **📊 Interactive Interface:** Provide a simple Streamlit interface with progress indicators and structured results.

## 🧠 System Architecture

CareerTwin AI combines Retrieval-Augmented Generation (RAG), semantic embeddings, vector similarity search, and local LLM inference.

### Architecture Overview

```text
             USER PROFILE
                   |
                   v
          Streamlit Interface
                   |
                   v
             app.py
                   |
          +--------+--------+
          |                 |
          v                 v
    Roadmap Memory     Profile Retrieval
      (FAISS)              |
          |                 v
          |          Sentence Transformers
          |          all-MiniLM-L6-v2
          |                 |
          |                 v
          |            FAISS Index
          |                 |
          |                 v
          |         Top 5 Similar Profiles
          |                 |
          +--------+--------+
                   |
                   v
               RAG Engine
                   |
                   v
             Ollama LLM
              GPT-OSS-20B
                   |
                   v
          Personalized Roadmap
                   |
                   v
            Save to Memory
                   |
                   v
            Streamlit Output
```

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | Interactive web interface |
| Sentence Transformers | Semantic embeddings |
| all-MiniLM-L6-v2 | Text embedding model |
| FAISS | Vector similarity search |
| NumPy | Numerical operations and embeddings |
| Ollama | Local LLM inference |
| GPT-OSS-20B | Career roadmap generation |
| RAG | Context-aware AI generation |

## 🔄 How It Works

**1. Data Preparation**

Professional profiles are transformed into semantic chunks containing information about:

- Personal information and LinkedIn profiles
- Professional experience
- Education
- Projects
- Skills
- Certifications
- Languages
- Volunteer experience

**2. Embedding Generation**

The `all-MiniLM-L6-v2` model converts semantic chunks into numerical vector representations.

Embeddings are normalized and stored for similarity search.

**3. FAISS Indexing**

FAISS creates a vector index using `IndexFlatIP` (Inner Product) to retrieve the most similar professional profiles.

**4. Profile Retrieval**

The user's profile is transformed into an embedding and compared against the indexed professional profiles.

The system retrieves the top 5 matching profiles.

**5. AI Roadmap Generation**

The RAG engine combines:
- User profile information.
- Retrieved professional profiles.
- A structured prompt defining the roadmap requirements.

GPT-OSS-20B generates a personalized career roadmap.

**6. Roadmap Memory**

Before generating a new roadmap, CareerTwin checks whether a sufficiently similar user profile already exists in its memory.

If the similarity score reaches the configured threshold (0.88), the existing roadmap is reused. Otherwise, a new roadmap is generated and stored.

## 📋 Generated Career Roadmap

The generated roadmap contains several structured sections:

| Section | Description |
|---|---|
| 🎯 Selected Best Profile | Best matching professional profile |
| 📘 User Context | Summary of the user's background |
| 🗺️ Career Roadmap | Short-term, mid-term, and long-term actions |
| 🛠️ Skills to Acquire | Missing skills and priorities |
| 🧰 Tools & Technologies | Recommended technologies |
| 📜 Certifications | Recommended certifications |
| 🧪 Portfolio Projects | Projects to strengthen the portfolio |
| 🧑‍🤝‍🧑 Networking Strategy | Professional networking recommendations |
| 💼 Jobs to Target | Suitable job positions |
| 🌟 Profile Insights | Lessons from the selected professional profile |

## 📁 Project Structure

```text
CareerTwin-AI/
│
├── app.py                  # Main application pipeline
├── streamlit_app.py        # Streamlit user interface
├── retrieval.py            # FAISS-based profile retrieval
├── rag_engine.py           # LLM and RAG generation
├── prompt.py               # Roadmap generation prompt
├── roadmap_memory.py       # Roadmap caching and memory
│
├── semantic_chunker.py     # Professional profile chunking
├── embed_profiles.py       # Embedding generation
├── build_faiss.py          # FAISS index creation
│
├── data/
│   └── scrap5_structured_final.json
│
├── career_twin_store/
│   ├── semantic_chunks.json
│   ├── chunks_meta.json
│   ├── embeddings.npy
│   └── faiss.index
│
├── roadmap_cache/
│   ├── meta.json
│   └── faiss.index
│
└── README.md
```
## 🎯 Project Objective

CareerTwin AI aims to make career development more intelligent and personalized by combining real-world professional experiences with modern AI technologies.

Instead of providing generic career advice, it uses semantic retrieval and LLM-powered generation to produce actionable career roadmaps aligned with each user's background and ambitions.

---

**Built with Python, RAG, FAISS, Sentence Transformers & Ollama.** 🚀
