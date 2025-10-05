# Vislona-Q-A-Chatbot
This is a dual-engine chatbot for Vislona to efficiently handle customer queries:
- 1.FAQ Engine (ML-based): Handles structured, repetitive questions.
- 2.Gemini API Engine: Handles open-ended or complex queries.
The chatbot will have a branded Streamlit web interface and will be accessible locally
via browser.

## Development

To set up the development environment and run the chatbot, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/subashrathlavath/Vislona-Q-A-Chatbot.git
   cd Vislona-Q-A-Chatbot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```
