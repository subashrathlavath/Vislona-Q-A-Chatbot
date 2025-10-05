import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

class Gemini_Engine:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')

    def get_response(self, query):
        try:
            response = self.model.generate_content(query)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"
