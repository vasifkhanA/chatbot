# Simple Interactive Django JSON Chatbot

This project contains **114 interactive questions**.

Features:
- Multiple answers for each question
- Random answer selection
- Follow-up questions
- Clickable interactive buttons
- Simple keyword matching
- Django + HTML + CSS + JavaScript + JSON
- No OpenAI/Gemini/external AI API

## Run

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Then:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open:
http://127.0.0.1:8000/

## Customize

Edit:

`data/knowledge.json`

Example:
```json
{
  "question": "What is Django?",
  "keywords": ["django", "framework"],
  "answers": [
    "Django is a Python web framework.",
    "Django is a popular Python framework."
  ],
  "follow_up": [
    "What are Django features?",
    "How do I install Django?"
  ]
}
```
