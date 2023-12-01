data = open("day1_data.txt", "r")
numbers_in_string = []
sum = 0
string_number = ""
number = 0
for line in data:
    print(line)
    for char in line:
        if char.isdigit():
            numbers_in_string.append(char)
    if len(numbers_in_string) == 1:
        string_number = "" + numbers_in_string[0] + numbers_in_string[0]
        sum += int(string_number)
    elif len(numbers_in_string) >> 1:
        string_number = "" + numbers_in_string[0] + numbers_in_string[len(numbers_in_string) - 1]
        sum += int(string_number)
    else:
        print("No Numbers.")

    numbers_in_string.clear()
print(sum)