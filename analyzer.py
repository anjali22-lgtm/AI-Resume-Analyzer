import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from prompts import PROMPT

# Load environment variables
load_dotenv()


print("API Key loaded:", bool(os.getenv("GOOGLE_API_KEY")))

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# Prompt template
prompt = PromptTemplate(
    template=PROMPT,
    input_variables=["resume", "job_description"]
)

# Create chain
chain = prompt | llm


def analyze_resume(resume_text, job_description):
    response = chain.invoke({
        "resume": resume_text,
        "job_description": job_description
    })

    return response.content