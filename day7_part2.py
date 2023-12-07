jack_used = False

def getData():
    file = open("day7_test_data.txt", "r")
    data = []
    for line in file:
        data.append(line.strip().split(" "))
    print(len(data))
    return data

def checkFiveOfAKind(hand):
    hand.sort()
    global jack_used
    print("Checking five", hand)
    if hand[0] == hand[4]:
        print("Five of a kind: " + str(hand))
        jack_used = False
        return True
    if checkFourOfAKind(hand) and 'J' in hand and jack_used == False:
        print("Five of a kind: " + str(hand))
        jack_used = True
        return True



def checkFourOfAKind(hand):
    hand.sort()
    global jack_used
    print("Checking four", hand)
    if hand[0] == hand[3] or hand[1] == hand[4]:
        print("Four of a kind: " + str(hand))
        jack_used = False
        return True
    elif 'J' in hand and checkThreeOfAKind(hand) and jack_used == False:
        print("Four of a kind: " + str(hand))
        jack_used = True
        return True

def checkFullHouse(hand):
    hand.sort()
    global jack_used
    print("Checking full", hand)
    if hand[0] == hand[2] and hand[3] == hand[4]:
        print("Full house: " + str(hand))
        jack_used = False
        return True
    elif hand[0] == hand[1] and hand[2] == hand[4]:
        print("Full house: " + str(hand))
        jack_used = False
        return True
    elif checkTwoPairs(hand) and 'J' in hand and jack_used == False:
        print("Full house: " + str(hand))
        jack_used = True
        return True
    elif hand.count('J') >= 2 and checkOnePair(hand):
        print("Full house: " + str(hand))

def checkThreeOfAKind(hand):
    hand.sort()
    global jack_used
    print("Checking three", hand)
    if hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]:
        print("Three of a kind: " + str(hand))
        jack_used = False
        return True
    if 'J' in hand and checkOnePair(hand) and jack_used == False:
        print("Three of a kind: " + str(hand))
        jack_used = True
        return True
    if hand.count('J') >= 2:
        jack_used = True
        return True

def checkTwoPairs(hand):
    hand.sort()
    global jack_used
    print("Checking two", hand)
    if hand[0] == hand[1] and hand[2] == hand[3]:
        print("Two pairs: " + str(hand))
        jack_used = False
        return True
    elif hand[0] == hand[1] and hand[3] == hand[4]:
        print("Two pairs: " + str(hand))
        jack_used = False
        return True
    elif hand[1] == hand[2] and hand[3] == hand[4]:
        print("Two pairs: " + str(hand))
        jack_used = False
        return True
    elif checkOnePair(hand) and 'J' in hand and jack_used == False:
        print("Two pairs: " + str(hand))
        jack_used = True
        return True
    elif hand.count('J') >= 2 and jack_used == False:
        print("Two pairs: " + str(hand))
        jack_used = True
        return True


def checkOnePair(hand):
    global jack_used
    hand.sort()
    print("Checking one", hand)
    if hand[0] == hand[1]:
        print("One pair: " + str(hand))
        jack_used = False
        return True
    elif hand[1] == hand[2]:
        print("One pair: " + str(hand))
        jack_used = False
        return True
    elif hand[2] == hand[3]:
        print("One pair: " + str(hand))
        jack_used = False
        return True
    elif hand[3] == hand[4]:
        print("One pair: " + str(hand))
        jack_used = False
        return True
    elif 'J' in hand and jack_used == False:
        print("One pair: " + str(hand))
        jack_used = True
        return True




def checkHighCard(hand):
    hand.sort()
    print("High card: " + str(hand))

card_value = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

data = getData()
max_rank = len(data)
results = []
print(max_rank)
for index, hand in enumerate(data):
    print()
    jack_used = False
    char_arr = []
    for char in hand[0]:
        char_arr.append(char)
    print("Hand and bet", hand)
    print("Hand", char_arr)
    if not checkFiveOfAKind(char_arr):
        if not checkFourOfAKind(char_arr):
            if not checkFullHouse(char_arr):
                if not checkThreeOfAKind(char_arr):
                    if not checkTwoPairs(char_arr):
                        if not checkOnePair(char_arr):
                            print("High card: " + str(hand))
                            jack_used = False
                            results.append([1, hand[1], hand[0]])
                            print("Append", 1)
                        else:
                            results.append([2, hand[1], hand[0]])
                            print("Append", 2)
                    else:
                        results.append([3, hand[1], hand[0]])
                        print("Append", 3)
                else:
                    results.append([4, hand[1], hand[0]])
                    print("Append", 4)
            else:
                results.append([5, hand[1], hand[0]])
                print("Append", 5)
        else:
            results.append([6, hand[1], hand[0]])
            print("Append", 6)
    else:
        results.append([7, hand[1], hand[0]])
        print("Append", 7)

print(len(results))

sorted_results = sorted(results, key=lambda x: x[0])
print("Len:", len(sorted_results), "Arr:", sorted_results)


def compare_hands(hand1, hand2):
    for index, char in enumerate(hand1):
        if card_value.index(hand1[index]) > card_value.index(hand2[index]):
            return -1
        elif card_value.index(hand1[index]) < card_value.index(hand2[index]):
            return 1
    return 0

def sort_results(results):
    sorted_results = results.copy() # Create a copy of the original array
    n = len(sorted_results)
    while True:
        swapped = False
        for index in range(n-1):
            if sorted_results[index][0] == sorted_results[index+1][0]:
                comparison = compare_hands(sorted_results[index][2], sorted_results[index+1][2])
                if comparison == -1:
                    sorted_results[index], sorted_results[index+1] = sorted_results[index+1], sorted_results[index]
                    swapped = True
        if not swapped:
            break
    return sorted_results

sorted_results = sort_results(sorted_results)


print(sorted_results)

sum = 0


for index, res in enumerate(sorted_results):
    sum += (index + 1) * int(res[1])
print("Len", len(sorted_results))
print(sum)
