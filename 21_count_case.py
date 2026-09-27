def count_case(text):
    upper = lower = digits = spaces = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
    return upper, lower, digits, spaces

u, l, d, s = count_case(input("Enter text: "))
print("Uppercase:", u)
print("Lowercase:", l)
print("Digits:", d)
print("Spaces:", s)
