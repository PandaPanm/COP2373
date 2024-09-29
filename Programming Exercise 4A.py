#Wes Williams

import time  # Importing the time module

# List of common spam keywords and phrases
SPAM_KEYWORDS = [
    "free", "winner", "money", "cash", "guarantee", "earn money", "increase sales", "credit",
    "loan", "save big", "make money", "congratulations", "gift", "click below", "urgent",
    "call now", "limited time", "exclusive deal", "lowest price", "risk-free", "apply now",
    "be your own boss", "100% free", "unsecured credit", "hot single locals!", "free trial", "free access",
    "single women in your area", "special promotion", "meet up", "discount"
]

def make_timer():
    """A timer function that returns a context manager for measuring elapsed time."""
    start_time = time.time()  # Record the start time
    yield  # Pause here, and resume when the timer is stopped
    elapsed_time = time.time() - start_time  # Calculate the elapsed time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")  # Print the elapsed time

def calculate_spam_score(message):
    score = 0
    detected_phrases = []

    # Convert message to lowercase for case-insensitive comparison
    message_lower = message.lower()

    for phrase in SPAM_KEYWORDS:
        if phrase in message_lower:
            score += 1
            detected_phrases.append(phrase)

    return score, detected_phrases

def assess_spam_likelihood(score):
    if score >= 20:
        return "Very Likely Spam"
    elif score >= 10:
        return "Likely Spam"
    elif score >= 5:
        return "Possible Spam"
    else:
        return "Unlikely Spam"

def main():
    print("Enter the email message to scan:")
    email_message = input()

    # Start the timer
    with make_timer():
        # Simulate processing time (if needed)
        time.sleep(1)  # Simulate a delay of 1 second

        spam_score, detected_phrases = calculate_spam_score(email_message)
        likelihood = assess_spam_likelihood(spam_score)

        print(f"\nSpam Score: {spam_score}")
        print(f"Likelihood of being spam: {likelihood}")
        if detected_phrases:
            print("Keywords/Phrases detected:")
            for phrase in detected_phrases:
                print(f" - {phrase}")

if __name__ == "__main__":
    main()
