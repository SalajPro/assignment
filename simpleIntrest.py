def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: SI = (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input principal amount, rate of interest, and time period
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Print simple interest
print("Simple Interest:", simple_interest)
