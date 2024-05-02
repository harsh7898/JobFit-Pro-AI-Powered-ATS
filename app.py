# import streamlit as st
# import google.generativeai as genai
# import os
# import PyPDF2 as pdf
# from dotenv import load_dotenv
# import json

# load_dotenv() ## load all our environment variables

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_repsonse(input):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content(input)
#     return response.text

# def input_pdf_text(uploaded_file):
#     reader=pdf.PdfReader(uploaded_file)
#     text=""
#     for page in range(len(reader.pages)):
#         page=reader.pages[page]
#         text+=str(page.extract_text())
#     return text

# def input_text(text):
#     return text

# #Prompt Template

# input_prompt="""
# I need you to be a very experience ATS (Application Tracking System) with a deep 
# understanding of IT field,software engineering,data science ,data analysts,
# data engineering, big data engineer, Machine Learning engineer, software development
# and all other Tech fields. Your task is to evaluate the resume based on the given job description.
# You must consider the job market is very competitive and you should provide 
# best assistance for improving the resumes. Assign the percentage Matching based 
# on Jd(Job Description) and the missing tech keywords with high accuracy
# resume:{text}
# description:{jd}
# """

# ## streamlit app
# st.title("JobFit Pro: AI-Powered ATS")
# st.text("Unlock your career potential with JobFit - where resumes find their perfect match.")

# jd = st.text_area("Paste the Job Description")
# uploaded_file = None
# text = None

# option = st.radio("Provide Resume:", ('Upload PDF', 'Paste Text'))

# if option == 'Upload PDF':
#     uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
# elif option == 'Paste Text':
#     text = st.text_area("Paste Your Resume Text Here")

# submit = st.button("Submit")

# if submit:
#     if uploaded_file is not None:
#         text = input_pdf_text(uploaded_file)
#     elif text is not None:
#         text = input_text(text)

#     if text is not None and jd.strip() != "":
#         input_prompt_filled = input_prompt.format(text=text, jd=jd)
#         response = get_gemini_repsonse(input_prompt_filled)
#         st.subheader(response)
#     else:
#         st.subheader("Please provide both resume text and job description.")


import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # Load environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def extract_text_from_pdf(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def process_text_input(text):
    return text

prompt_template = """
I need you to be a very experience ATS (Application Tracking System) with a deep 
understanding of IT field,software engineering,data science ,data analysts,
data engineering, big data engineer, Machine Learning engineer, software development
and all other Tech fields. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on Jd(Job Description) and the missing tech keywords with high accuracy.
Always highlight and increase the font of percentage matching

Resume Text: {text}
Job Description: {jd}
"""

# Streamlit app
st.title("JobFit Pro: AI-Powered ATS")
st.text("Unlock your career potential with JobFit - where resumes find their perfect match.")

job_description = st.text_area("Paste the Job Description")
uploaded_resume = None
resume_text = None

option = st.radio("Select Resume Input Method:", ('Upload PDF', 'Paste Text'))

if option == 'Upload PDF':
    uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload your resume in PDF format")
elif option == 'Paste Text':
    resume_text = st.text_area("Paste Your Resume Text Here")

submit_button = st.button("Evaluate")

if submit_button:
    if uploaded_resume is not None:
        resume_text = extract_text_from_pdf(uploaded_resume)
    elif resume_text is not None:
        resume_text = process_text_input(resume_text)

    if resume_text is not None and job_description.strip() != "":
        filled_prompt = prompt_template.format(text=resume_text, jd=job_description)
        response = get_gemini_response(filled_prompt)
        st.subheader("Evaluation Result:")
        st.write(response)
    else:
        st.subheader("Please provide both resume text and a job description.")

