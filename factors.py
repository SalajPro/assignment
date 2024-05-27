def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input a number
number = int(input("Enter a number: "))

# Calculate factorial
fact = factorial(number)

# Print factorial
print("Factorial of", number, "is:", fact)
