def count_words(text):
    count = 0
    inside = False
    for ch in text:
        if ch != " " and not inside:
            count += 1
            inside = True
        elif ch == " ":
            inside = False
    return count

print("Words =", count_words(input("Enter sentence: ")))
