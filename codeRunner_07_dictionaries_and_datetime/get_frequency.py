
def get_frequencies(filename):

    frequencies = {}

    with open(filename) as f:
        for line in f:
            for char in line.lower():
                if char.isalpha() and ord(char) < 128:
                    if char in frequencies:
                        frequencies[char] += 1
                    else:
                        frequencies[char] = 1

    return frequencies


if __name__ == "__main__":
    frequencies = get_frequencies("wordlist.txt")

    print("Letter Frequency")

    for letter, frequency in sorted(frequencies.items()):
        print(f"   {letter:<3} {frequency:>5}")
    


