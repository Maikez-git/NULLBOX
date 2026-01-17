"""
simulator.py

Simulates the logical effect of an injection attack
WITHOUT executing any real code, queries, or commands.
"""

def simulate_attack(attack_type: str, lab: str) -> dict:
    """
    Simulates what would happen if this attack were successful
    in a vulnerable real-world application.

    Returns:
        dict with simulated outcome
    """

    # Default safe response
    simulation = {
        "success": False,
        "impact": "No impact",
        "details": "No malicious behavior detected."
    }

    if attack_type == "SQL Injection":
        if lab == "login":
            simulation = {
                "success": True,
                "impact": "Authentication Bypass",
                "details": (
                    "The injected condition always evaluates to TRUE, "
                    "allowing access without valid credentials."
                )
            }
        else:
            simulation = {
                "success": True,
                "impact": "Database Manipulation",
                "details": (
                    "The injected SQL could expose or modify database records "
                    "in a vulnerable application."
                )
            }

    elif attack_type == "Cross-Site Scripting (XSS)":
        simulation = {
            "success": True,
            "impact": "Client-Side Script Execution",
            "details": (
                "The injected script would execute in the victim’s browser, "
                "potentially stealing cookies or performing actions on their behalf."
            )
        }

    elif attack_type == "Command Injection":
        simulation = {
            "success": True,
            "impact": "Remote Command Execution",
            "details": (
                "The injected command could execute system-level commands "
                "on the server if input is not properly sanitized."
            )
        }

    return simulation
