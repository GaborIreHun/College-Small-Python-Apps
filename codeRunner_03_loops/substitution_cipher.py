
from string import ascii_lowercase

# variable for user input
plain_text = input("Enter a message to encipher: ").lower()

# variable for result string
ciphertext = ""

# checking for characters
for character in plain_text:

    # validating characters and building result string
    if not character.isalpha():
        ciphertext += character
    elif ascii_lowercase.index(character) % 2 == 0:
        index_number = ascii_lowercase.index(character)
        ciphertext += ascii_lowercase[index_number + 1]
    else:
        index_number = ascii_lowercase.index(character)
        ciphertext += ascii_lowercase[index_number - 1]

# printing the result string
print("The enciphered message is: ", ciphertext)
