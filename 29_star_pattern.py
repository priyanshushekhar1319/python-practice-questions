def star_pattern(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print("*", end="")
        print()

star_pattern(int(input("Enter n: ")))
