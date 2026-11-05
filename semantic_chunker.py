import json
import os

STORE_DIR = "career_twin_store"

def semantic_chunk_profile(profile):
    chunks = []

    identity = f"""
    Name: {profile.get('Full_name')}
    Headline: {profile.get('headline')}
    About: {profile.get('about')}
    Location: {profile.get('city')}, {profile.get('country_code')}
    LinkedIn: {profile.get('profile_url')}
    """
    chunks.append(identity.strip())

    for job in profile.get("experience", []):
        ch = f"""
        EXPERIENCE
        Name: {profile.get('Full_name')}
        Company: {job.get('company')}
        Title: {job.get('title')}
        Description: {job.get('description')}
        Start: {job.get('start_date')}
        End: {job.get('end_date')}
        URL: {job.get('url')}
        """
        chunks.append(ch.strip())

        for pos in job.get("positions", []):
            p = f"""
            EXPERIENCE (Internal Role)
            Company: {job.get('company')}
            Title: {pos.get('title')}
            Description: {pos.get('description')}
            Start: {pos.get('start_date')}
            End: {pos.get('end_date')}
            """
            chunks.append(p.strip())

    for edu in profile.get("education", []):
        chunks.append(f"""
        EDUCATION
        School: {edu.get('school')}
        Degree: {edu.get('degree')}
        Field: {edu.get('field')}
        Years: {edu.get('start_year')} - {edu.get('end_year')}
        """.strip())

    for proj in profile.get("projects", []):
        chunks.append(f"""
        PROJECT
        Title: {proj.get('title')}
        Description: {proj.get('description')}
        Start: {proj.get('start_date')}
        """.strip())

    for c in profile.get("certifications", []):
        chunks.append(f"""
        CERTIFICATION
        Title: {c.get('title')}
        Organization: {c.get('organization')}
        Date: {c.get('date')}
        """.strip())

    if profile.get("skills"):
        chunks.append("SKILLS: " + ", ".join(profile["skills"]))

    if profile.get("languages"):
        chunks.append("LANGUAGES:\n" + "\n".join(
            f"{l['language']}: {l['description']}" for l in profile["languages"]
        ))

    for v in profile.get("volunteer_experience", []):
        chunks.append(f"""
        VOLUNTEERING
        Organization: {v.get('organization')}
        Title: {v.get('title')}
        Duration: {v.get('duration')}
        """.strip())

    return chunks



def semantic_chunk_dataset(input_file):
    os.makedirs(STORE_DIR, exist_ok=True)

    profiles = json.load(open(input_file, "r", encoding="utf-8"))
    all_chunks = []

    for idx, p in enumerate(profiles):
        chunks = semantic_chunk_profile(p)
        for c in chunks:
            all_chunks.append({
                "profile_id": idx,
                "chunk": c,
                "name": p.get("Full_name"),
                "url": p.get("profile_url"),
                "about": p.get("about")   # added for UI
            })

    out_path = os.path.join(STORE_DIR, "semantic_chunks.json")
    json.dump(all_chunks, open(out_path, "w", encoding="utf-8"), indent=2)

    print("Semantic chunking complete.")
    print("Stored:", out_path)
    print("Total chunks:", len(all_chunks))


if __name__ == "__main__":
    semantic_chunk_dataset("data/scrap5_structured_final.json")
