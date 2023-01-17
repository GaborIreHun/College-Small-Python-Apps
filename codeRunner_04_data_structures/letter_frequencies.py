from string import ascii_lowercase

sentence = input("Enter the text: ").lower()

letter = list(ascii_lowercase)

most_frequent_letter = ""

highest_value = 0

frequency = [0] * 26

for character in sentence:
    for c in letter:
        if character == c:
            frequency[ascii_lowercase.index(c)] += 1

for i in range(26):
    if i == 0:
        most_frequent_letter = letter[0]
        highest_value = frequency[0]
    else:
        if frequency[i] > frequency [i-1] and frequency[i] > highest_value:
            most_frequent_letter = letter[i]
            highest_value = frequency[i]


print("\nLetter Frequency")
for letter,frequency in zip(ascii_lowercase,frequency):
    print(f"{letter:^5}{frequency:^9}")

print()
print("Most frequent letter: ", most_frequent_letter)
