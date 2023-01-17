
states = []
members_retiring = []
dates_of_retirement = []
mean = 0.0
mode = 0.0
median = 0

file_name = input("Enter the filename: ")

try:
    with open(file_name, "r") as data_file:

        _ = data_file.readline()

        for line in data_file:

            try:
                state, member_retiring, date_of_retirement = line.split(",")
            except ValueError:
                print("Line has invalid format:", line)
                continue
            try:
                states.append(state)
                members_retiring.append(int(member_retiring))
                dates_of_retirement.append(date_of_retirement)
            except ValueError:
                print("Invalid or missing number of members for", state)
                continue

    uniques = sorted(set(members_retiring))
    sorted_members_retiring = sorted(members_retiring)
    frequencies = [members_retiring.count(value) for value in uniques]
    max_frequencies = max(frequencies)
    max_freq_index = frequencies.index(max_frequencies)

    mean = sum(members_retiring)/len(members_retiring)
    mode = uniques[max_freq_index]

    try:
        if len(sorted_members_retiring) % 2 == 0:
            med1 = sorted_members_retiring[len(sorted_members_retiring)//2]
            med2 = sorted_members_retiring[len(sorted_members_retiring)//2 - 1]
            median = (med1 + med2)/2
        else:
            median = sorted_members_retiring[len(sorted_members_retiring)//2]
    except ZeroDivisionError:
        print("Invalid or missing number of members for", state)

    print(f"Mean Members Retiring per State: {mean:.1f}")
    print(f"Median Members Retiring per State: {median:.1f}")
    print("Mode of Members Retiring per State:", mode)

except FileNotFoundError:
    print("Unable to open the file", file_name)







