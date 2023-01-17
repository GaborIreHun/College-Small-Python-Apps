import datetime

users_date = input("Enter a date in the form dd/mm/yyyy: ")

day, month, year = map(int, users_date.split('/'))

formatted_date = datetime.date(year, month, day)

day_of_the_week = formatted_date.strftime('%A')

print("Day of the week:", day_of_the_week)
