def is_palindrome(string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
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

    # Check if the input is a palindrome
    if is_palindrome(user_input):
        print("The input is a palindrome.")
    else:
        print("The input is not a palindrome.")

    # Display the input in reverse order
    reversed_string = user_input[::-1]
    print("Reversed string: " + reversed_string)

    # Count the number of characters in the input
    char_count = len(user_input)
    print(f"Number of characters: {char_count}")

    # Convert the input to uppercase
    uppercase_string = user_input.upper()
    print("Uppercase: " + uppercase_string)

    # Convert the input to lowercase
    lowercase_string = user_input.lower()
    print("Lowercase: " + lowercase_string)

    # Print symbol values
    print_symbol_values(user_input)

    # Print indices of numeric digits
    print_numeric_indices(user_input)

    # Print indices of vowels
    print_vowel_indices(user_input)

if __name__ == "__main__":
    main()
