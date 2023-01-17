
contacts = ["087 1234567", "090 9876543", "090 6468000", "112"]

while True:

    request = input("[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()

    if request == "p":
        print("Numbers in your contacts list")
        for index,number in enumerate(contacts):
            print(index,":",number)
        print()

    elif request == "c":
        is_there = False
        number_to_check = input("Enter the number: ")
        for number in contacts:
            if number == number_to_check:
                is_there = True
                print("Number {} is in the list".format(number_to_check))
                print()
        if is_there == False:
            print("Number {} is not in the list".format(number_to_check))
            print()

    elif request == "a":
        number_to_add = input("Enter new number: ")
        contacts.append(number_to_add)
        print("Added {} to the list".format(number_to_add))
        print()

    elif request == "e":
        number_to_edit = input("Enter number to edit: ")
        new_number = input("Enter the new number: ")
        contacts[contacts.index(number_to_edit)] = new_number
        print("Replaced {} with {}".format(number_to_edit, new_number))
        print()

    elif request == "d":
        number_to_delete = input("Enter number to delete: ")
        contacts.remove(number_to_delete)
        print("Removed {} from the list".format(number_to_delete))
        print()

    elif request == "q":
        break

