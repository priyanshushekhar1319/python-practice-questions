def first_character(text):
    for ch in text:
        print(ch)
        break

text = input("Enter text: ")
first_character(text) if text else print("String is empty")
