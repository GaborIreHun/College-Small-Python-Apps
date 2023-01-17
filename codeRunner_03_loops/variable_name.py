
# variable for user input
variables = input("Enter the variable name: ")

# counter for print decision
counter = 0

# invalid variable
invalid_variable = ''

# foreach to check characters of input
for variable in variables:

    # validating character
    if not variable.isalpha() and not variable.isdigit() and not variable == '_' or variable == '-':
        invalid_variable += variable
        counter += 1

# checking if there is an invalid character and printing appropriate message
if counter == 0:
    print("Valid variable name")
else:
    print("Invalid character ", invalid_variable)




