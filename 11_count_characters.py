def count_characters(text):
    count = 0
    for _ in text:
        count += 1
    return count

print("Characters =", count_characters(input("Enter text: ")))
