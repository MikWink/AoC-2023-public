data = open("day1_data.txt", "r")
numbers_in_string = []
for line in data:
    print(line)
    for char in line:
        if char.isdigit():
            numbers_in_string.insert(char)

    print(numbers_in_string)