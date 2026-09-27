def find_longest_word(text):
    longest = current = ""
    for ch in text + " ":
        if ch != " ":
            current += ch
        else:
            if len(current) > len(longest):
                longest = current
            current = ""
    return longest

print("Longest word =", find_longest_word(input("Enter sentence: ")))
