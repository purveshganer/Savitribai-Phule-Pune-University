def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def print_symbol_values(string):
    print("Symbol values:")
    for char in string:
        if not char.isalnum():
            print(f"{char}: {ord(char)}")

def print_numeric_indices(string):
    print("Indices of numeric digits:")
    for i, char in enumerate(string):
        if char.isdigit():
            print(f"Index {i}: {char}")

def print_vowel_indices(string):
    print("Indices of vowels:")
    vowels = "aeiouAEIOU"
    for i, char in enumerate(string):
        if char in vowels:
            print(f"Index {i}: {char}")

def main():
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The input is a palindrome.")
    else:
        print("The input is not a palindrome.")

    reversed_string = user_input[::-1]
    print("Reversed string: " + reversed_string)

    char_count = len(user_input)
    print(f"Number of characters: {char_count}")

    uppercase_string = user_input.upper()
    print("Uppercase: " + uppercase_string)

    lowercase_string = user_input.lower()
    print("Lowercase: " + lowercase_string)
    print_symbol_values(user_input)
    print_numeric_indices(user_input)
    print_vowel_indices(user_input)

if __name__ == "__main__":
    main()
