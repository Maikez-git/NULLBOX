"""
explainer.py

Generates educational explanations for each type of attack.
Each explanation is tailored to the lab context (login, comment, etc.)
"""

def generate_explanation(attack_type: str, lab: str, payload: str) -> str:
    """
    Returns a human-readable explanation based on attack type and lab context.
    """

    payload_display = payload.replace("<", "&lt;").replace(">", "&gt;")  # safe HTML display

    if attack_type == "SQL Injection":
        return (
            f"Detected SQL Injection in the {lab} lab.\n"
            f"The payload <code>{payload_display}</code> attempts to manipulate the database query.\n"
            f"For example, in a login form, this could bypass authentication if used on a real system."
        )

    elif attack_type == "Cross-Site Scripting (XSS)":
        return (
            f"Detected XSS attack in the {lab} lab.\n"
            f"The payload <code>{payload_display}</code> could execute scripts in the victim's browser.\n"
            f"For example, in a comment box, this could steal session cookies on a real site."
        )

    elif attack_type == "Command Injection":
        return (
            f"Detected Command Injection in the {lab} lab.\n"
            f"The payload <code>{payload_display}</code> could execute system commands if used in unsafe backend code.\n"
            f"For example, it might list files or read sensitive information."
        )

    else:  # Benign / no injection
        return f"No injection detected. The payload <code>{payload_display}</code> appears safe."

