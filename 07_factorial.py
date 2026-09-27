def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter number: "))
print("Factorial =", factorial(n) if n >= 0 else "Not possible")
