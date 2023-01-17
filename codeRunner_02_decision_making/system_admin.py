
space = int(input("Enter total space: "))

amount_used= int(input("Enter amount used: "))

perc_of_free_space = 1 - (amount_used / space)

if perc_of_free_space < 0:
    print("Invalid input")
elif perc_of_free_space == 0:
    print("The percentage free space is 0.0%")
    print("Warning: system full")
elif perc_of_free_space < 0.05:
    print(f"The percentage free space is {perc_of_free_space*100:.1f}%")
    print("Warning, low disk space")
else:
    print(f"The percentage free space is {perc_of_free_space*100:.1f}%")
    print("System has sufficient disk space")



