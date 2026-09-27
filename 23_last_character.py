def last_character(text):
    last = ""
    for ch in text:
        last = ch
    return last

text = input("Enter text: ")
if text:
    print("Using -1:", text[-1])
    print("Using loop:", last_character(text))
else:
    print("String is empty")
