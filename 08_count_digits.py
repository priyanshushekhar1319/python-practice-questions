def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n:
        n //= 10
        count += 1
    return count

print("Digits =", count_digits(int(input("Enter number: "))))
