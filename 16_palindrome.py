def check_palindrome(text):
    return text == text[::-1]

text = input("Enter text: ")
print("Palindrome" if check_palindrome(text) else "Not Palindrome")
