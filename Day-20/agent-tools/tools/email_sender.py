from langchain.tools import tool

@tool
def send_email(to: str, subject: str, message: str) -> str:
    """
    Simulates sending an email.
    Inputs:
    - to: recipient email
    - subject: email subject
    - message: email content
    """
    try:
        if not to or "@" not in to:
            return "Error: Invalid email address"

        if not subject:
            return "Error: Subject cannot be empty"

        if not message:
            return "Error: Message cannot be empty"

        # Simulated sending
        return f"""
Email Sent Successfully

To: {to}
Subject: {subject}
Message: {message}
"""

    except Exception as e:
        return f"Error sending email: {str(e)}"