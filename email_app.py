import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from gmail_service import get_unread_emails, send_reply
from ai_service import generate_reply

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    emails = get_unread_emails()
    return render_template("dashboard.html", emails=emails)


@app.route("/reply", methods=["POST"])
def reply():
    email_text = request.form["email_text"]
    to_email = request.form["to_email"]

    try:
        ai_reply = generate_reply(email_text)
    except Exception as e:
        ai_reply = "Auto-reply: Thank you for your email. I'll get back to you soon."

    send_reply(to_email, ai_reply)

    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(debug=True)
