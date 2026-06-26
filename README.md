# Vislona Q&A Chatbot

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An intelligent dual-engine chatbot for Vislona that efficiently handles customer queries by routing them to specialized AI systems. Combines an ML-based FAQ engine for quick, accurate responses to common questions with Google's Gemini API for complex, open-ended discussions.

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Dual-Engine Architecture**: Intelligently routes queries to the most appropriate handler
  - **FAQ Engine**: Fast, ML-based responses for structured and repetitive questions
  - **Gemini API Engine**: Contextual, nuanced responses for complex and open-ended queries
- **Branded Streamlit UI**: Clean, professional web interface accessible locally
- **Easy Integration**: Simple setup process with minimal dependencies
- **Efficient Query Handling**: Optimized performance for customer support scenarios

## 🏗️ Architecture

```
User Query
    ↓
Query Classifier
    ↓
    ├── FAQ Engine (ML-based) ────→ Structured Questions
    │
    └── Gemini API Engine ────→ Complex/Open-ended Questions
    ↓
Response
```

The chatbot analyzes incoming queries and determines whether they're best handled by:
1. The **FAQ Engine** - for pattern-matched, frequently asked questions
2. The **Gemini API Engine** - for nuanced responses requiring AI reasoning

## 📦 Prerequisites

- **Python**: 3.8 or higher
- **pip**: Package installer for Python
- **Gemini API Key**: [Get it from Google AI Studio](https://makersuite.google.com/app/apikey)
- **Internet Connection**: Required for Gemini API engine

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/subashrathlavath/Vislona-Q-A-Chatbot.git
cd Vislona-Q-A-Chatbot
```

### 2. Create and Activate Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

Alternatively, set the environment variable:

**Windows:**
```bash
set GEMINI_API_KEY=your_api_key_here
```

**macOS/Linux:**
```bash
export GEMINI_API_KEY=your_api_key_here
```

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The chatbot will open in your default web browser at `http://localhost:8501`

### Using the Chatbot

1. Enter your question in the text input field
2. The chatbot will automatically route your query to the appropriate engine
3. Receive an instant response with the source indicated (FAQ Engine or Gemini API)

### Example Queries

**FAQ Engine (Structured):**
- "What are your business hours?"
- "How do I reset my password?"
- "What is your return policy?"

**Gemini API Engine (Complex):**
- "Can you explain how your product compares to competitors?"
- "What would be the best approach for my specific use case?"
- "Help me troubleshoot this complex issue I'm facing"

## 📁 Project Structure

```
Vislona-Q-A-Chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── config/               # Configuration files
│   └── faq_data.json    # FAQ database
├── engines/              # Core chatbot engines
│   ├── faq_engine.py    # ML-based FAQ handler
│   └── gemini_engine.py # Gemini API handler
├── utils/                # Utility functions
│   └── query_router.py   # Query classification logic
└── README.md            # This file
```

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "API key not found" or authentication errors

**Solution:** Verify your Gemini API key is correctly set:
```bash
# Check if environment variable is set (macOS/Linux)
echo $GEMINI_API_KEY

# Check if .env file exists and is in project root
ls -la | grep .env
```

### Issue: Streamlit app not opening in browser

**Solution:** Manually navigate to `http://localhost:8501` in your browser, or check console output for the correct URL.

### Issue: Slow responses from Gemini API

**Solution:** 
- Check your internet connection
- Verify API rate limits haven't been exceeded
- Consider caching FAQ responses

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Code Standards
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Include unit tests for new features
- Update README.md with significant changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For issues, questions, or suggestions, please:
- Open an [GitHub Issue](https://github.com/subashrathlavath/Vislona-Q-A-Chatbot/issues)
- Contact the maintainer

---

**Last Updated:** 2026  
**Version:** 1.0.0
