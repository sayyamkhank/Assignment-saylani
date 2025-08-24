##Write a program that accepts a string from user. Your program should count and display number of
#vowels in that string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print("Number of vowels in the string:", vowel_count)

"""Write a program that reads a string from keyboard and display:
* The number of uppercase letters in the string
* The number of lowercase letters in the string
* The number of digits in the string
* The number of whitespace characters in the string"""

def analyze_string(input_string):
    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())
    digit_count = sum(1 for char in input_string if char.isdigit())
    whitespace_count = sum(1 for char in input_string if char.isspace())

    return uppercase_count, lowercase_count, digit_count, whitespace_count

user_input = input("Enter a string: ")
upper, lower, digits, whitespace = analyze_string(user_input)

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
print("Number of digits:", digits)
print("Number of whitespace characters:", whitespace)

"""Write a Python program that accepts a string from user. Your program should create and display a
new string where the first and last characters have been exchanged"""

def exchange_first_last(input_string):
    if len(input_string) < 2:
        return input_string  # No change for single-character strings
    # Exchange the first and last characters
    new_string = input_string[-1] + input_string[1:-1] + input_string[0]
    return new_string

user_input = input("Enter a string: ")
result = exchange_first_last(user_input)
print("New string with exchanged characters:", result)

"""Write a Python program that accepts a string from user. Your program should create a new string in
reverse of first string and display it"""

def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Enter a string: ")
reversed_result = reverse_string(user_input)
print("Reversed string:", reversed_result)

"""Write a Python program that accepts a string from user. Your program should create a new string by
shifting one position to left"""

def shift_left(input_string):
    if len(input_string) < 2:
        return input_string  # No change for single-character strings
    # Shift all characters to the left by one position
    new_string = input_string[1:] + input_string[0]
    return new_string

user_input = input("Enter a string: ")
shifted_result = shift_left(user_input)
print("New string after shifting left:", shifted_result)

"""Write a program that asks the user to input his name and print its initials. Assuming that the user
always types first name, middle name and last name and does not include any unnecessary spaces"""

def print_initials(full_name):
    names = full_name.split()
    initials = [name[0].upper() for name in names]
    print("Initials:", " ".join(initials))

user_input = input("Enter your full name: ")
print_initials(user_input)

"""A palindrome is a string that reads the same backward as forward. For example, the words dad,
madam and radar are all palindromes. Write a programs that determines whether the string is a
palindrome.
Note: do not use reverse() method"""

def is_palindrome(input_string):
    # Check if the string is equal to its reverse
    for i in range(len(input_string) // 2):
        if input_string[i] != input_string[-(i + 1)]:
            return False
    return True

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

"""Write a program that display following output:
SHIFT
HIFTS
IFTSH
FTSHI
TSHIF
SHIFT"""

def display_shifted_strings(input_string):
    for i in range(len(input_string)):
        print(input_string[i:] + input_string[:i])

user_input = input("Enter a string: ")
display_shifted_strings(user_input)

"""Write a program in python that accepts a string to setup a passwords. Your entered password must
meet the following requirements
The password must be at least eight characters long.
It must contain at least one uppercase letter.
It must contain at least one lowercase letter.
It must contain at least one numeric digit.
Your program should should perform this validation."""

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

user_input = input("Enter a password: ")
if is_valid_password(user_input):
    print("Password is valid.")
else:
    print("Password is invalid.")
