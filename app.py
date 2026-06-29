import streamlit as st
from parser import extract_resume_text
from analyzer import analyze_resume

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# Header
# -----------------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#4CAF50;'>
        🤖 AI Resume Analyzer
    </h1>
    <h4 style='text-align:center; color:gray;'>
        Analyze your Resume using Gemini AI + LangChain
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------------
# Resume Upload
# -----------------------------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------
# Job Description
# -----------------------------------
job_description = st.text_area(
    "💼 Paste Job Description",
    height=250,
    placeholder="Paste the complete job description here..."
)
# -----------------------------------
# Analyze Button
# -----------------------------------
if st.button("🚀 Analyze Resume", use_container_width=True):

    if uploaded_file is None:
        st.warning("⚠️ Please upload your resume.")

    elif job_description.strip() == "":
        st.warning("⚠️ Please paste the job description.")

    else:
        # Extract Resume Text
        resume_text = extract_resume_text(uploaded_file)

        st.success("✅ Resume uploaded successfully!")

        # AI Analysis
        with st.spinner("🤖 AI is analyzing your resume... Please wait..."):
            result = analyze_resume(
                resume_text,
                job_description
            )

        # Success Animation
        st.balloons()
        st.success("🎉 Analysis completed successfully!")

        st.divider()

        # AI Result
        st.subheader("📊 AI Analysis")

        st.markdown(result)

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray; font-size:14px;'>
        ❤️ Developed by <b>Anjali Jamwal</b><br><br>
        🤖 AI Resume Analyzer using Gemini AI • LangChain • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)