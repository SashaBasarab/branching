def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year (between 2016 and 2024): "))

if year < 2016 or year > 2024:
    print("Invalid year. Please enter a year between 2016 and 2024.")
    exit(1)

if is_leap_year(year):
    print(f"{year} є високосним роком.")
else:
    print(f"{year} не є високосним роком.")
