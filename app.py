import streamlit as st
from pypdf import PdfReader
from skills import extract_skills
from scorer import calculate_score
from missing_skills import find_missing_skills
from feedback import generate_feedback

st.title("SkillMatch AI")
st.subheader("AI-Powered Resume Screening System")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    skills_found = extract_skills(text)

    job_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Power BI",
        "AWS"
    ]

    score = calculate_score(skills_found, job_skills)
    missing = find_missing_skills(skills_found, job_skills)
    feedback = generate_feedback(score, missing)
    st.success("Resume uploaded successfully!")

    st.write("### Skills Found")
    st.write(skills_found)

    st.write("### Match Score")
    st.write(f"{score}%")
    st.progress(int(score))
    
    st.write("### Missing Skills")
    st.write(missing)
    
    st.write("### Feedback")
    st.write(feedback)