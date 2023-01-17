from random import randint

# user's total
total = 0

# counter for the rolls
counter = 0

# loop to roll the dice 3 times
while counter < 3:

    # current value of rolled dice
    current_roll = randint(1, 6)
    # print the current value of rolled dice
    print("You rolled: ", current_roll)
    # incrementing total with rolled value
    total += current_roll
    # incrementing counter
    counter += 1

# printing total
print("Total rolled: ", total)

# printing appropriate result
if total >= 10:
    print("You win!")
else:
    print("You lose")




