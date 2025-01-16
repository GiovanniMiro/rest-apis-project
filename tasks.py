import os
import requests
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
API_KEY = os.getenv("MAILGUN_API_KEY")

def send_simple_message(to, subject, body):
    #if not domain or not api_key:
    #    raise ValueError("Environment variable for Mailgun are not set properly.")
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth=("api", API_KEY),
        data={
            "from": f"Your name <mailgun@{DOMAIN}>",
            "to": [to],
            "subject": subject,
            "text": body}
    )

def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API"
    )