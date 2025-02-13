age=int(input("Enter age: "))
max_age = 90
years_remaining = max_age - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left until age 90.")
