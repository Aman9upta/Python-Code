def factorial_recursive(n):
    if n < 0:
        return "Undefined"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

numbers = [2, 4, 6]
factorials = [factorial_recursive(num) for num in numbers]
print(factorials)