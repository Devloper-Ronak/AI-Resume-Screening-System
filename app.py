import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_resume_text
from skill_matcher import extract_skills, calculate_ats_score
from recommender import recommend_roles

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#f8fafc;
}

.hero{
    padding:30px;
    border-radius:20px;
    background:linear-gradient(90deg,#2563eb,#3b82f6);
    text-align:center;
    margin-bottom:20px;
}

.hero h1{
    color:white;
    font-size:50px;
}

.hero p{
    color:white;
    font-size:18px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.08);
}

.small-card{
    background:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.05);
    text-align:center;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
<h1>🚀 AI Career Mentor</h1>
<p>Smart Resume Screening • ATS Analysis • Career Guidance</p>
</div>
""", unsafe_allow_html=True)

left,right = st.columns(2)

with left:

    uploaded_resume = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

with right:

    job_description = st.text_area(
        "📝 Job Description",
        height=220,
        placeholder="""
Looking for Full Stack Developer with:
HTML
CSS
JavaScript
React
Flask
Git
GitHub
SQL
"""
    )

st.write("")

if st.button("🚀 Analyze Resume", use_container_width=True):

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter a job description.")
        st.stop()

    resume_text = extract_resume_text(uploaded_resume)

    if len(resume_text.strip()) == 0:
        st.error("Unable to extract text from PDF.")
        st.stop()

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    ats_score = calculate_ats_score(
        resume_skills,
        jd_skills
    )

    roles = recommend_roles(resume_skills)

    st.subheader("📊 Dashboard")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("🎯 ATS Score", f"{ats_score}%")
    c2.metric("💻 Skills", len(resume_skills))
    c3.metric("✅ Matched", len(matched))
    c4.metric("❌ Missing", len(missing))

    st.progress(int(ats_score))

    st.subheader("👤 Candidate Profile")

    profile_left, profile_right = st.columns([1,3])

    with profile_left:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=130
        )

    with profile_right:

        st.info("""
Name: Ronak Khan

Role: Full Stack Developer

Education: B.Tech Computer Science

Career Goal: Full Stack + AI Engineer
""")

    chart1, chart2 = st.columns(2)

    with chart1:

        chart_data = pd.DataFrame({
            "Category":["Matched","Missing"],
            "Count":[len(matched),len(missing)]
        })

        fig = px.pie(
            chart_data,
            values="Count",
            names="Category",
            title="Skill Match Analysis"
        )

        st.plotly_chart(fig, use_container_width=True)

    with chart2:

        st.subheader("📈 Career Insights")

        if ats_score >= 85:

            st.success("""
Excellent Resume Match

Your profile strongly aligns with the target role.
""")

        elif ats_score >= 70:

            st.info("""
Good Resume Match

Add more backend/database skills.
""")

        else:

            st.warning("""
Needs Improvement

Increase project quality and relevant skills.
""")

    colA,colB = st.columns(2)

    with colA:

        st.subheader("✅ Matched Skills")

        for skill in matched:
            st.success(skill)

    with colB:

        st.subheader("❌ Missing Skills")

        if missing:

            for skill in missing:
                st.warning(skill)

        else:
            st.success("No Missing Skills")

    st.subheader("💼 Recommended Roles")

    for role in roles:
        st.info(role)

    st.subheader("🛣 Learning Roadmap")

    if missing:

        for skill in missing:
            st.write(f"📚 Learn {skill}")

    else:

        st.success(
            "You match all required skills."
        )

    st.subheader("💻 Extracted Skills")

    st.write(", ".join(resume_skills))

    with st.expander("🔍 View Extracted Resume Text"):

        st.text(resume_text[:5000])