
current_password = input("Enter current password: ")

new_password = input("Enter new password: ")

re_new_password = input("Re-enter new password: ")

if current_password == new_password or len(new_password) < 8 or new_password != re_new_password:
    print("Password change unsuccessful")
elif new_password == re_new_password:
    print("Password changed")

