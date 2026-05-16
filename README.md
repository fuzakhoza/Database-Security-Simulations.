# Secure Coding Lab: SQL Injection Mitigation in Python

## 🎯 Objective
This project demonstrates how insecure user input handling leads to structural SQL Injection (SQLi) vulnerabilities, and provides the programmatic defense mechanism required to neutralize data exposure risks.

## ⚠️ The Vulnerability (Insecure String Concatenation)
In the initial build, user input was directly integrated into the database query structure:
```python
query = f"SELECT * FROM users WHERE username = '{user_input}';"
```
*   **The Exploit:** Inputting `' OR '1'='1` manipulates the query logic to evaluate as always true, bypassing authentication controls and exposing the entire user table database.

## 🛡️ The Remediation (Parameterized Queries)
To safely mitigate this vulnerability, the system was refactored to implement parameterized placeholders (`?`). This isolates user input structurally, preventing the database engine from executing input strings as operational commands:
```python
query = "SELECT * FROM users WHERE username = ?;"
cursor.execute(query, (user_input,))
```

## 🛠️ Environment & Tools
*   **OS:** Kali Linux
*   **Language:** Python 3.x
*   **Database Engine:** SQLite3
