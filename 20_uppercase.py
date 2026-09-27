def convert_uppercase(text):
    result = ""
    for ch in text:
        result += chr(ord(ch) - 32) if "a" <= ch <= "z" else ch
    return result

text = input("Enter text: ")
print("Using upper():", text.upper())
print("Using loop:", convert_uppercase(text))
