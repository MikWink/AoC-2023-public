strings = open("day4_data.txt", "r")


sum = 0

def calcCopiesOfCards(data, reps, line_index):
    sum = 0

    for index, line in enumerate(data):
        if index == line_index:
            if reps > 0:
                line_index += 1
                reps -= 1

            #print(line)
            win_num = []
            norm_num = []
            counter = 0
            print("Copied Card:", line.strip())
            numbers = line[9:].strip().split(" ")

            divider = False
            for num in numbers:
                if num == "|":
                    divider = True
                if divider == False:
                    win_num.append(num)
                elif divider == True and not num == "|":
                    norm_num.append(num)

            #print("Win:", win_num, "Norm:", norm_num)

            for w in win_num:
                for n in norm_num:
                    if w == n and w.isnumeric() and n.isnumeric():
                        #print(w, "==", n, "?")
                        #print("Counter+")
                        counter += 1
            #print("Counter:", counter)
            if counter == 0:
                result = 0
            elif counter > 0:
                print()


    return sum


for index, line in enumerate(data):
    #print(line)
    win_num = []
    norm_num = []
    counter = 0
    print(line.strip())
    numbers = line[9:].strip().split(" ")

    divider = False
    for num in numbers:
        if num == "|":
            divider = True
        if divider == False:
            win_num.append(num)
        elif divider == True and not num == "|":
            norm_num.append(num)

    print("Win:", win_num, "Norm:", norm_num)

    for w in win_num:
        for n in norm_num:
            if w == n and w.isnumeric() and n.isnumeric():
                print(w, "==", n, "?")
                print("Counter+")
                counter += 1
    print("Counter:", counter)
    if counter == 0:
        result = 0
    elif counter > 0:
        print(calcCopiesOfCards(data, counter, index))
        result = pow(2, counter - 1)
        sum += result
        print("Result:", result, "Sum:", sum)



print("Ergebnis:", sum)
