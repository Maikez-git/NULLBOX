"""
patterns.py

Contains regex patterns for detecting common injection attacks.
These patterns are intentionally conservative to reduce false positives.
"""

# =========================
# SQL Injection Patterns
# =========================
SQLI_PATTERNS = [
    r"('|\")\s*or\s*('|\")?\d+=\d+",          # ' OR 1=1
    r"('|\")\s*or\s*('|\")?.+?('|\")?=('|\")?.+",  # ' OR 'a'='a'
    r"union\s+select",                        # UNION SELECT
    r"select\s+.+\s+from",                    # SELECT * FROM table
    r"insert\s+into\s+.+\s+values",           # INSERT INTO table VALUES
    r"update\s+.+\s+set",                     # UPDATE table SET
    r"delete\s+from",                         # DELETE FROM
    r"--",                                    # SQL comment
    r"#",                                     # MySQL comment
    r"/\*"                                   # /* comment start
]

# =========================
# Cross-Site Scripting (XSS)
# =========================
XSS_PATTERNS = [
    r"<\s*script.*?>.*?<\s*/\s*script\s*>",   # <script>...</script>
    r"<\s*script.*?>",                         # <script>
    r"on\w+\s*=",                              # onerror=, onclick=
    r"javascript\s*:",                         # javascript:
    r"<\s*img.*?src\s*=",                      # <img src=...
    r"<\s*iframe.*?>",                         # <iframe>
    r"document\.cookie",                      # document.cookie
    r"alert\s*\(",                             # alert(
]

# =========================
# Command Injection
# =========================
CMD_INJECTION_PATTERNS = [
    r";\s*[\w\-]+",                            # ; ls
    r"\|\s*[\w\-]+",                           # | cat
    r"&&\s*[\w\-]+",                           # && whoami
    r"\b(cat|ls|pwd|whoami|id)\b",             # common commands
    r"\$\(.+\)",                               # $(command)
    r"`.+?`",                                  # `command`
]
