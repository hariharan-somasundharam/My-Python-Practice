def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

while True:
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
