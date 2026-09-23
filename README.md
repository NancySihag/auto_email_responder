# AI Email Responder

🚀 **Live Demo:** [Try the Auto Email Responder](https://auto-email-responder-npnj.onrender.com)

A Flask-based email automation demo that combines OpenAI-powered reply generation with a Gmail-style email dashboard.

The project demonstrates how AI can be integrated into an email workflow to generate professional responses from incoming messages.

> **Note:** The current version uses mock email data and a simulated send function for safe local development. Gmail API integration is structured in the project but is not currently used by the dashboard.

---

## Features

- 📧 Email dashboard for reviewing incoming messages
- 🤖 AI-generated professional email replies using OpenAI
- ⚡ One-click reply workflow
- 🛡️ Environment-based API key configuration
- 🔄 Fallback response when AI generation fails
- 🧪 Test-ready project structure
- 🌐 Flask web application with reusable HTML templates

---

## Tech Stack

- **Language:** Python 3.12
- **Backend:** Flask
- **AI:** OpenAI API
- **Email Integration:** Gmail API libraries
- **Frontend:** HTML, CSS, JavaScript
- **Configuration:** python-dotenv
- **Testing:** pytest

---

## Project Structure

```text
auto_email_responder/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── .python-version
│
├── email_app.py
├── ai_service.py
├── gmail_service.py
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
└── tests/

Incoming Email
      ↓
Email Dashboard
      ↓
Extract Email Content
      ↓
OpenAI Reply Generation
      ↓
Professional Reply
      ↓
Send Reply
