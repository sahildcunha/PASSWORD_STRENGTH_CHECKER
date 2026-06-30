import re
import math

def check_password_strength(password: str) -> dict:
    """
    This function evaluates how strong a password is.
    It returns:
    - score (numerical strength)
    - entropy (randomness estimate)
    - feedback (suggestions to improve password)
    - strength label (Weak / Moderate / Strong)
    """

    # Dictionary to store all results of analysis
    result = {
        "score": 0,          # final calculated strength score
        "max_score": 7,      # maximum possible score
        "feedback": [],      # list of suggestions for user
        "strength": ""       # final label (Weak, Strong, etc.)
    }

    # -----------------------------
    # 1. LENGTH ANALYSIS
    # -----------------------------
    # Longer passwords are harder to crack, so we reward length
    length = len(password)

    if length >= 16:
        result["score"] += 2  # very strong length bonus
    elif length >= 12:
        result["score"] += 1  # moderate length bonus
        result["feedback"].append("Consider 16+ characters for stronger security")
    elif length >= 8:
        result["feedback"].append("Minimum met, but 12+ characters recommended")
    else:
        result["feedback"].append("Too short — use at least 8 characters")

    # -----------------------------
    # 2. CHARACTER VARIETY CHECK
    # -----------------------------
    # A strong password should include multiple types of characters:
    # lowercase, uppercase, numbers, and special symbols
    checks = [
        (r'[a-z]', "lowercase letter"),
        (r'[A-Z]', "uppercase letter"),
        (r'\d', "digit"),
        (r'[!@#$%^&*(),.?\":{}|<>_\-\[\]\\\/`~;\'+=]', "special character"),
    ]

    for pattern, name in checks:
        # If pattern is found, increase score
        if re.search(pattern, password):
            result["score"] += 1
        else:
            # If missing, suggest improvement
            result["feedback"].append(f"Add a {name}")

    # -----------------------------
    # 3. WEAK PATTERN DETECTION
    # -----------------------------
    # This section detects common insecure patterns like:
    # repeated characters, sequences, and commonly used passwords
    weak_patterns = [
        (r'(.)\1{2,}', "repeated characters (aaa, 111)"),
        (r'(012|123|234|345|456|567|678|789|890)', "sequential numbers"),
        (r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', "sequential letters"),
        (r'(qwerty|asdf|zxcv|password|admin|login|welcome)', "common patterns"),
    ]

    for pattern, description in weak_patterns:
        # Convert password to lowercase to catch all variations
        if re.search(pattern, password.lower()):
            result["score"] -= 1  # penalize weak patterns
            result["feedback"].append(f"Avoid {description}")

    # -----------------------------
    # 4. ENTROPY CALCULATION
    # -----------------------------
    # Entropy measures how unpredictable a password is.
    # Higher entropy = harder to crack.
    charset_size = 0

    # Determine which types of characters are used
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        charset_size += 32

    # Calculate entropy using formula:
    # entropy = length * log2(charset size)
    entropy = length * math.log2(charset_size) if charset_size > 0 else 0
    result["entropy_bits"] = round(entropy, 1)

    # -----------------------------
    # 5. FINAL SCORE CLASSIFICATION
    # -----------------------------
    # Convert raw score into human-readable strength label
    score = max(0, result["score"])  # prevent negative scores

    if score >= 6:
        result["strength"] = "Strong"
    elif score >= 4:
        result["strength"] = "Moderate"
    elif score >= 2:
        result["strength"] = "Weak"
    else:
        result["strength"] = "Very Weak"

    # Store final score back into result
    result["score"] = score

    return result


# -----------------------------
# 6. MAIN PROGRAM (USER INPUT)
# -----------------------------
if __name__ == "__main__":

    # Display program title
    print("🔐 Password Strength Checker")
    print("-" * 30)

    # Take password input from user
    # NOTE: In real secure apps, use getpass() so password is hidden
    password = input("Enter your password: ")

    # Run password analysis function
    analysis = check_password_strength(password)

    # -----------------------------
    # OUTPUT SECTION
    # -----------------------------
    print("\n--- Analysis Result ---")
    print(f"Strength: {analysis['strength']} ({analysis['score']}/{analysis['max_score']})")
    print(f"Entropy: ~{analysis['entropy_bits']} bits")

    # Print suggestions if any exist
    if analysis["feedback"]:
        print("Feedback:")
        for f in analysis["feedback"]:
            print(f" - {f}")
