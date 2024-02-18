import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
prompt = 'I need JSON data extracted from the provided CV. The CV follows this format: {"projects": [{"title": "", "description": "", "tech_stack": [], "time_duration": {"start": "04-2020", "end": "05-2020", "duration_months": 2}, "relevancy": 5}], "experience": [{"role": "", "organization": "", "short_description": "", "tech_stack": [], "time_duration": {"start": "05-2022", "end": "07-2022", "duration_months": 3}, "relevancy": 4}], "college": {"name": "IIT Bombay", "branch": "Electrical Engineering", "degree": "Dual Degree", "cgpa": 8.2, "start": "07-2018", "end": "05-2023"}}. Below is The cv:'


def get_gemini_response(question):
    question = prompt + "\n\n" + question
    response = chat.send_message(question, stream=True)
    return response
