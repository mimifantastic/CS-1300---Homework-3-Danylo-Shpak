# CS 1300 - Homework 3
# Danylo Shpak
# Filename follows the assignment's coding-file instructions.

# Problem 1: User Profile Generator
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ")

first_name = first_name.title()
last_name = last_name.title()
hobby = hobby.title()
age = 2026 - birth_year

print("=" * 36)
print("         USER PROFILE CARD")
print("=" * 36)
print(f"Name:    {first_name} {last_name}")
print(f"Age:     {age}")
print(f"Hobby:   {hobby}")
print("-" * 36)
print("Thank you for creating your profile!")
print("=" * 36)

# Problem 2: Text Analyzer
print("\n=== TEXT ANALYZER ===")
sentence = input("Enter a sentence: ")

total_with_spaces = len(sentence)
total_without_spaces = len(sentence.replace(" ", ""))
number_of_words = len(sentence.split())
vowels = 0
for character in sentence.lower():
    if character in "aeiou":
        vowels += 1

uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
reversed_sentence = sentence[::-1]

if len(sentence) > 0 and sentence[0].isupper():
    starts_with_capital = "Yes"
else:
    starts_with_capital = "No"

if len(sentence) > 0 and sentence[-1] in ".!?":
    ends_with_punctuation = "Yes"
else:
    ends_with_punctuation = "No"

print("--- Analysis Results ---")
print(f"Total characters (with spaces): {total_with_spaces}")
print(f"Total characters (without spaces): {total_without_spaces}")
print(f"Number of words: {number_of_words}")
print(f"Number of vowels: {vowels}")
print(f"Uppercase version: {uppercase_sentence}")
print(f"Lowercase version: {lowercase_sentence}")
print(f"Reversed: {reversed_sentence}")
print(f"Starts with capital: {starts_with_capital}")
print(f"Ends with punctuation: {ends_with_punctuation}")

# Bonus Question 46: Palindrome Checker
word = input("\nEnter a word or phrase: ")
cleaned_word = word.replace(" ", "").lower()
reversed_word = cleaned_word[::-1]
if cleaned_word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")
