# Password Strength Checker

**Intern ID:** CITS 4048

A simple Python-based Password Strength Checker that evaluates the security of a password using common cybersecurity best practices. This project was developed as part of a Cybersecurity & Ethical Hacking internship and tested using Python IDLE.

---

## Overview

The program analyzes a password based on the following criteria:

- Password length
- Presence of lowercase letters
- Presence of uppercase letters
- Presence of numbers
- Presence of special characters
- Detection of common weak passwords (e.g., `password`, `admin`, `123456`)
- Detection of repeated characters (e.g., `aaa`, `111`)
- Detection of sequential numbers (e.g., `123`, `456`)
- Detection of sequential letters (e.g., `abc`, `def`)
- Password entropy calculation
- Password improvement suggestions

---

## How It Works

The program uses Python's built-in `re` (Regular Expressions) module to analyze password patterns and `math.log2()` to estimate password entropy.

The evaluation process includes:

1. Checking password length
2. Checking character diversity
3. Detecting weak patterns
4. Calculating password entropy
5. Assigning a strength rating

---

## Strength Ratings

Based on the final score, the password is classified as:

- Very Weak
- Weak
- Moderate
- Strong

The program also displays:

- Score (out of 7)
- Password entropy
- Suggestions to improve password strength

---

## How to Run

### 1. Install Python

Ensure Python 3.x is installed on your computer.

### 2. Open the Project

Open the `passwordStrengthChecker.py` file using Python IDLE or any Python IDE.

### 3. Run the Program

In Python IDLE:

```
Run → Run Module (F5)
```

### 4. Enter a Password

When prompted:

```
Enter your password:
```

The program will analyze the password and display:

- Strength Rating
- Score
- Entropy
- Improvement Suggestions

---

## Requirements

- Python 3.x

No external libraries are required.

### Built-in Modules Used

- `re`
- `math`

---

## Project Structure

```
PASSWORD_STRENGTH_CHECKER/
│
├── passwordStrengthChecker.py
└── README.md
```

---

## Learning Outcomes

This project demonstrates:

- Password security analysis
- Regular Expressions (Regex)
- Entropy calculation
- Conditional logic
- User input handling
- Cybersecurity best practices in Python

---

## Author

**Intern ID:** CITS 4048

Developed as part of a Cybersecurity & Ethical Hacking Internship.
