
number_of_copies = int(input("Enter number of copies: "))

cost = 0

if number_of_copies > 0 and number_of_copies < 51:
   cost = number_of_copies * .11
elif number_of_copies > 50 and number_of_copies < 101:
   cost = number_of_copies * .10
elif number_of_copies > 100 and number_of_copies < 1001:
   cost = number_of_copies * .09
elif number_of_copies > 1000:
   cost = number_of_copies * .08

print(f"Cost is {cost :.2f}")
