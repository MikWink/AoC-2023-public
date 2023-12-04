def readData(string):
    line_arr = []
    for index, line in enumerate(string):
        line_arr.append(line[9:].strip())
    return line_arr

def splitLine(line):
    win_num = []
    norm_num = []
    divider = False
    numbers_bad = line.strip().split(" ")
    numbers = [item for item in numbers_bad if not item.isspace() and item != ""]
    for num in numbers:
        if num == "|": divider = True
        if divider == False:
            win_num.append(num)
        elif divider == True and not num == "|":
            norm_num.append(num)
    return win_num, norm_num

def checkWinning(win, norm):
    counter = 0
    for w in win:
        for n in norm:
            if w == n:
                counter += 1

    return counter

string = open("day4_data.txt")


data_arr = readData(string)
scratchers = 0
copies = 0
cardCount = []
for i in range(len(data_arr)):
    cardCount.append(1)

for index, card in enumerate(data_arr):

    count = 0
    print("=" * 10, "Card:", index + 1, "=" *10)
    win_num, norm_num = splitLine(card)
    count = checkWinning(win_num, norm_num)
    #print("Win Counter:", count)
    for i in range(count):
        cardCount[index + i + 1] += cardCount[index]
        print(cardCount, "Index:", index + i +1)

print("Sum:", sum(cardCount))
