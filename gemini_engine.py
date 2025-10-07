import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

class Gemini_Engine:
    def __init__(self, model_name="gemini-2.5-flash", system_instruction=None):
        self.model_name = model_name
        
        self.system_instruction = system_instruction or (
            "You are a precise customer-support assistant for Vislona. "
            "When asked about Vislona-specific details, prefer concise factual answers and ask clarifying questions only if absolutely necessary."
        )

    def get_response(self, user_query, context_history=None):
        """
        context_history: list of dicts like [{"role":"user","content":...}, {"role":"model","content":...}]
        """
        try:
            model = genai.GenerativeModel(
                self.model_name,
                system_instruction=self.system_instruction
            )
            
            messages = []
            if context_history:
                for item in context_history:
                    messages.append({"role": item["role"], "parts": [item["content"]]})
            messages.append({"role": "user", "parts": [user_query]})

            response = model.generate_content(messages)
            return response.text
        except Exception as e:
            return f"Gemini error: {e}"
