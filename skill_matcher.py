skills_db = [
    "python","java","c++","javascript","html","css",
    "react","node.js","node","flask","django",
    "mysql","mongodb","sql","git","github",
    "machine learning","deep learning","ai",
    "numpy","pandas","matplotlib","bootstrap",
    "tailwind","aws","docker","linux"
]

def extract_skills(text):

    found = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return sorted(list(set(found)))


def calculate_ats_score(resume_skills, jd_skills):

    if len(jd_skills) == 0:
        return 0

    matched = list(set(resume_skills) & set(jd_skills))

    score = (len(matched) / len(jd_skills)) * 100

    return round(score, 2)