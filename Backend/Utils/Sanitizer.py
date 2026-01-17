"""
sanitizer.py

Handles basic sanitization and validation of user input.
Prevents accidental execution and ensures safe analysis.
"""

MAX_PAYLOAD_LENGTH = 500


def sanitize_payload(payload: str) -> str:
    """
    Sanitizes user input payload for safe processing.

    Steps:
    - Ensure payload is a string
    - Trim excessive whitespace
    - Enforce length limit
    - Do NOT execute or evaluate anything
    """

    if payload is None:
        return ""

    # Force string type
    payload = str(payload)

    # Strip leading/trailing whitespace
    payload = payload.strip()

    # Enforce max length
    if len(payload) > MAX_PAYLOAD_LENGTH:
        payload = payload[:MAX_PAYLOAD_LENGTH]

    return payload


def is_payload_valid(payload: str) -> bool:
    """
    Basic validation check for payload.
    Returns False if payload is empty after sanitization.
    """

    if not payload:
        return False

    return True
