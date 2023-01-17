import re

file = open("error.log", "r")
count = 0
count2 = 0
missing_files = []

while True:

    line = file.readline()

    match = re.findall("(File does not exist:)", line)

    match2 = re.findall("(/+\w+/+\w+/+\w+/+\w+/+\w+\.+\w)", line)

    for m in match2:
        if m not in missing_files:
            missing_files.append(m)

    if match:
        count += 1

    if not line:
        break

print("Number of missing file errors:",count)
print("Number of unique missing files:",len(missing_files))