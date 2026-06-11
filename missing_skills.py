def find_missing_skills(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))