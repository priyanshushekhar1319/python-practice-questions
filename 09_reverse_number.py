def reverse_number(n):
    reverse = 0
    n = abs(n)
    while n:
        reverse = reverse * 10 + n % 10
        n //= 10
    return reverse

print("Reverse =", reverse_number(int(input("Enter number: "))))
