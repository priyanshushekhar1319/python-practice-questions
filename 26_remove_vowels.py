def remove_vowels(text):
    result = ""
    for ch in text:
        if ch not in "aeiouAEIOU":
            result += ch
    return result

print(remove_vowels(input("Enter text: ")))
