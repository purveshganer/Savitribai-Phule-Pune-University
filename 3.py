import re

# Prompt the user for input
user_input = input("Enter a string: ")

# Define a list of syntactical patterns
patterns = [
    r'\b\w+\b',  # Match words
    r'\b\d+\b',  # Match numbers
    r'\b\d{2}-\d{2}-\d{4}\b',  # Match dates in the format "dd-mm-yyyy"
    r'\b[A-Z][a-z]+\b',  # Match capitalized words
    r'\b\w*ed\b',  # Match words ending with "ed"
]

# Generate patterns from the user input
for pattern in patterns:
    matches = re.findall(pattern, user_input)
    if matches:
        print(f"Pattern '{pattern}': {', '.join(matches)}")
