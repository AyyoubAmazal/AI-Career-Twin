import streamlit as st
from app import run_careertwin
import time

st.set_page_config(page_title="CareerTwin AI", page_icon="🎯", layout="wide")
st.title("🎯 CareerTwin – AI Career Roadmap Generator")

st.markdown("Enter your profile to generate a personalized AI-powered career roadmap based on the best matching LinkedIn profile.")

name = st.text_input("👤 Name")
skills = st.text_area("🧠 Skills (comma separated)").split(",")
experience = st.text_area("💼 Experience")
education = st.text_input("🎓 Education")
languages = st.text_area("🌐 Languages (comma separated)").split(",")
certifications = st.text_area("📜 Certifications (comma separated)").split(",")
goals = st.text_input("🚀 Career Goal")

if st.button("Generate Roadmap"):
    
    user = {
        "name": name,
        "skills": skills,
        "experience": experience,
        "education": education,
        "languages": languages,
        "certifications": certifications,
        "goals": goals
    }

    # ----------------------------
    # PROGRESS BAR SECTION
    # ----------------------------
    progress = st.progress(0)
    status = st.empty()

    # Step 1: Preparing Data
    status.markdown("🔄 Preparing your profile…")
    time.sleep(0.5)
    progress.progress(10)

    # Step 2: FAISS Retrieval
    status.markdown("🔍 Searching for best matching profiles…")
    result = run_careertwin(user)
    progress.progress(65)

    # Step 3: LLM Generation
    status.markdown("🤖 Generating your personalized roadmap…")
    time.sleep(0.8)
    progress.progress(100)

    status.success("✨ Roadmap generated successfully!")

    st.markdown("---")

    # ----------------------------
    # STRUCTURED OUTPUT RENDERING
    # ----------------------------
    roadmap = result["roadmap"]

    # Add section titles with emojis
    st.markdown("## 🧭 Your Complete Career Roadmap")
    st.markdown(roadmap)

    st.markdown("---")
    st.markdown("### 💡 Tip: You can improve your roadmap by adding more details to your profile such as education, experience, and goals.")
