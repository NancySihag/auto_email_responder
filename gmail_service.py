def get_unread_emails():
    # Return dummy data for UI testing first
    return [
        {
            "text": "Hi, can you share pricing?",
            "email": "test@gmail.com"
        },
        {
            "text": "I need support with my account",
            "email": "user@gmail.com"
        }
    ]


def send_reply(to_email, message):
    print(f"Sending reply to {to_email}: {message}")