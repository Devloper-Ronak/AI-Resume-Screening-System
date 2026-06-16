def recommend_roles(skills):

    roles = []

    if "react" in skills and "javascript" in skills:
        roles.append("Frontend Developer")

    if "python" in skills:
        roles.append("Python Developer")

    if "react" in skills and ("flask" in skills or "node.js" in skills):
        roles.append("Full Stack Developer")

    if "machine learning" in skills or "ai" in skills:
        roles.append("ML Engineer")

    return roles