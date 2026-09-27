def count_vowels_consonants(text):
    vowels = consonants = 0
    for ch in text:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

v, c = count_vowels_consonants(input("Enter text: "))
print("Vowels =", v)
print("Consonants =", c)
