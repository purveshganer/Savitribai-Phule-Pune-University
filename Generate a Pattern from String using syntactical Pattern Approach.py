import re

user_input = input("Enter a string: ")
patterns = [r'\b\w+\b',r'\b\d+\b',r'\b\d{2}-\d{2}-\d{4}\b',r'\b[A-Z][a-z]+\b',r'\b\w*ed\b',]
for pattern in patterns:
    matches = re.findall(pattern, user_input)
    if matches:
        print(f"Pattern '{pattern}': {', '.join(matches)}")
