def checkLeftNeighbours(line, index):
    reversed_number = ""
    while index > 0 and not line[index] == ".":
        index -= 1
        if line[index].isdigit():
            reversed_number += line[index]
    if reversed_number:
        return int(reversed_number[::-1])
    else:
        return 0

def checkRightNeighbours(line, index):
    number = ""
    while index < (len(line) - 1) and not line[index] == ".":
        index += 1
        if line[index].isdigit():
            number += line[index]
    if number:
        return int(number)
    else:
        return 0

def checkTopNeighbours(data, line_index, line, char_index):

    if not line_index == 0:
        numbers = getNumbersInLine(data[line_index - 1])
        print(numbers)
        return 0
    return 0

def getNumbersInLine(line):
    numbers = []
    number = ""
    for index, char in enumerate(line):
        if char.isdigit():
            number += char
        elif char == "." or char == "\n":
            numbers.append(number)
    return numbers

data = open("day3_data.txt", "r")
lines = []
for lin in data:
    lines.append(lin)
sum = 0
for index, line in enumerate(data):
    print("Line", index, ":", line)
    for index2, char in enumerate(line):
        if not char.isdigit() and not char == "." and not char == "\n":
            print("Symbol", char, "found at position", index2, "in line", index)
            if checkLeftNeighbours(line, index2) > 0:
                print("Found left Neighbour:", checkLeftNeighbours(line, index2))
                sum += checkLeftNeighbours(line, index2)
            else:
                print("no left Neighbour found.")
            if checkRightNeighbours(line, index2) > 0:
                print("Found left Neighbour:", checkRightNeighbours(line, index2))
                sum += checkRightNeighbours(line, index2)
            else:
                print("no right Neighbour found.")
            if checkTopNeighbours(lines, index, line, index2) > 0:
                print("Found top Neighbour:", checkTopNeighbours(lines, index, line, index2))
                sum += checkTopNeighbours(lines, index, line, index2)
            else:
                print("no top Neighbour found.")


print("Ergebnis:", sum)