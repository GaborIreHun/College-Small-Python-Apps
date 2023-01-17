fullname = input("Enter your first and last names, separated by a space: ")
firstname, lastname = fullname.split()
username = firstname.lower() + (lastname[:1]).lower()
print("Your username is: " + username)