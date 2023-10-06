import math
while True:
    num1 = int(input("Enter num 1:"))
    num2 = int(input("Enter num 2:"))

    gcd = math.gcd(num1, num2)
    print("GCD of", num1, "and", num2, "is", gcd)
