def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

multiplication_table(int(input("Enter number: ")))
