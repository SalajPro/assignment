def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Input from user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print("It's a leap year")
else:
    print("Not a leap year")
