def character_frequency(text, ch):
    count = 0
    for x in text:
        if x == ch:
            count += 1
    return count

text = input("Enter text: ")
ch = input("Enter character: ")
print("Frequency =", character_frequency(text, ch))
