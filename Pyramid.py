def print_pyramid(rows):
    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(" ", end="")
        for j in range(0, i + 1):
            print("* ", end="")
        print()
rows = int(input("Enter the range:"))
print_pyramid(rows)
