def generate_feedback(score, missing_skills):
    
    if score >= 80:
        feedback = "Excellent match for the job role."
    elif score >= 60:
        feedback = "Good match, but some skills are missing."
    else:
        feedback = "Needs significant improvement for this role."

    return f"""
Feedback:
{feedback}

Missing Skills:
{', '.join(missing_skills)}

Recommendation:
Try learning the missing skills and add related projects to your resume.
"""