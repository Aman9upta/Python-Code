a = input("Enter a 4-digit number: ")
if not a.isdigit() or len(a) != 4:
    print("Please enter a valid 4-digit number.")
else:
    num = int(a)
    power = len(a)
    total = sum(int(digit) ** power for digit in a)

    if total == num:
        print(a, "is a narcissistic number")
    else:
        print(a, "is not a narcissistic number")