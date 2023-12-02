def part1(input):
    numbers_in_string = []
    puzzle_answer = 0
    string_number = ""
    number = 0
    for line in input:
        print(line)
        for char in line:
            if char.isdigit():
                numbers_in_string.append(char)
        if len(numbers_in_string) == 1:
            string_number = "" + numbers_in_string[0] + numbers_in_string[0]
            puzzle_answer += int(string_number)
        elif len(numbers_in_string) >> 1:
            string_number = "" + numbers_in_string[0] + numbers_in_string[len(numbers_in_string) - 1]
            puzzle_answer += int(string_number)
        else:
            print("No Numbers.")

        numbers_in_string.clear()
    print(puzzle_answer)


def part2(input):
    numbers_in_string = []
    puzzle_answer = 0
    int_as_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    found_string = ""
    found_string2 = ""


    for line in input:
        found_string = ""
        found_string2 = ""
        print(line)
        pos1 = 500
        pos2 = 0
        for num in int_as_words:
            if line.find(num) >= 0:
                if pos1 > line.find(num):
                    pos1 = line.find(num)
                    found_string = num
            if line.rfind(num) >= 0:
                if pos2 <= line.rfind(num):
                    pos2 = line.rfind(num)
                    found_string2 = num



        print("First found Number at pos ", pos1, " : ", found_string, ", last found Number at pos ", pos2, " : ", found_string2)

        if len(found_string) == 1 and len(found_string2) == 1:
            print("" + found_string + found_string2)
            puzzle_answer += int(("" + found_string + found_string2))
        elif len(found_string) >> 1 and len(found_string2) >> 1:
            counter = 1
            digit1 = ""
            digit2 = ""
            for x in int_as_words:
                if x == found_string:
                    digit1 = str(counter)
                if x == found_string2:
                    digit2 = str(counter)
                counter = counter + 1
            print("" + digit1 + digit2)
            puzzle_answer += int(("" + digit1 + digit2))
        elif len(found_string) >> 1 and len(found_string2) == 1:
            counter = 1
            digit1 = ""
            for x in int_as_words:
                if x == found_string:
                    digit1 = str(counter)
                counter = counter + 1
            print("" + digit1 + found_string2)
            puzzle_answer += int("" + digit1 + found_string2)
        elif len(found_string) == 1 and len(found_string2) >> 1:
            counter = 1
            digit2 = ""
            for x in int_as_words:
                if x == found_string2:
                    digit2 = str(counter)
                counter = counter + 1
            print("" + found_string + digit2)
            puzzle_answer += int("" + found_string + digit2)

    return(puzzle_answer)



data = open("day1_data.txt", "r")
print(part2(data))
