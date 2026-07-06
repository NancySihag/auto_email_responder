# AI-Powered Gmail Auto-Responder 🤖📧

An intelligent Flask web application that connects directly to your Gmail account to fetch unread emails, automatically craft context-aware responses using AI, and send replies instantly with a single click.

---

## ✨ Features

*   **Unread Email Dashboard:** Automatically fetches and displays incoming unread emails.
*   **AI-Generated Replies:** Processes email body text using an advanced AI language model to generate smart, natural-sounding drafts.
*   **Instant Sending:** One-click reply handling that routes generated messages directly back to the sender.
*   **Graceful Fallback:** Includes error-handling loops that use a polite, generic auto-reply if the AI service encounters an issue.

---

## 🛠️ Tech Stack

*   **Backend:** Python 3 (Flask Framework)
*   **Email Integration:** Gmail API / Google Client Library (`gmail_service.py`)
*   **AI Engine:** OpenAI GPT / Google Gemini API (`ai_service.py`)
*   **Frontend UI:** HTML & CSS Templates (`index.html`, `dashboard.html`)

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.8 or higher installed on your local machine.
*   A Google Cloud Project with the **Gmail API** enabled and OAuth 2.0 credentials set up.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/nancysihag631-stack/ai_resume_analyzer.git](https://github.com/nancysihag631-stack/ai_resume_analyzer.git)
   cd ai_resume_analyzer
