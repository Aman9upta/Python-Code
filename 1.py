# write  a function  to find the maximum of two number
# input : two number
def find_max(a, b):
    return max(a, b)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The maximum number is:", find_max(num1, num2))
