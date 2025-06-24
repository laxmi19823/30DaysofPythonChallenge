def factorial(n):
    if n == 0 or n == 1:                        # Base case
        return 1
    return n * factorial(n - 1)                # Recursive call

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
