# Function to check if a year is a leap year
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Function to find the number of days in a month for a given year
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month < 1 or month > 12:
        return "Invalid month"
    
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

# Example usage:
year = 2024
month = 2
print(days_in_month(year, month))  # Output: 29

year = 2022
month = 2
print(days_in_month(year, month))  # Output: 28

year = 2023
month = 4
print(days_in_month(year, month))  # Output: 30

#from google....
