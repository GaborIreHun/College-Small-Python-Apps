# storing user input
values_string = input("Enter a series of numbers, separated by spaces: ")

# populating number_list from input
numbers_list = [int(i) for i in values_string.split() ]

# initializing total
number_of_values = len(numbers_list)

# initializing total
total = 0

# calculating total
for i in numbers_list:
    total += i

# defining mean
mean = '{0:.1f}'.format(total / number_of_values)

# helper variable for min and max
sorted_number_list = sorted(numbers_list)

# defining maximum
maximum = sorted_number_list[len(sorted_number_list) - 1]

# defining minimum
minimum = sorted_number_list[0]

print("Number of values:", number_of_values)
print("Total:", total)
print("Mean:", mean)
print("Maximum:", maximum)
print("Minimum:", minimum)
