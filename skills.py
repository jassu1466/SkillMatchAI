SKILLS = [
    "Python",
    "SQL",
    "Machine Learning",
    "Power BI",
    "Java",
    "AWS",
    "Data Science",
    "Excel"
]

def extract_skills(text):
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
