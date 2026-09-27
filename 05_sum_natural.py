def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Sum =", sum_natural(int(input("Enter n: "))))
