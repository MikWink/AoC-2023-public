def getData():
    file = open("day7_data.txt", "r")
    data = []
    for line in file:
        data.append(line.strip().split(" "))

    return data

def checkFiveOfAKind(hand):
    hand.sort()
    if hand[0] == hand[4]:
        print("Five of a kind: " + str(hand))
        return True

def checkFourOfAKind(hand):
    hand.sort()
    if hand[0] == hand[3] or hand[1] == hand[4]:
        print("Four of a kind: " + str(hand))
        return True

def checkFullHouse(hand):
    hand.sort()
    if hand[0] == hand[2] and hand[3] == hand[4]:
        print("Full house: " + str(hand))
        return True
    elif hand[0] == hand[1] and hand[2] == hand[4]:
        print("Full house: " + str(hand))
        return True

def checkThreeOfAKind(hand):
    hand.sort()
    if hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]:
        print("Three of a kind: " + str(hand))
        return True

def checkTwoPairs(hand):
    hand.sort()
    if hand[0] == hand[1] and hand[2] == hand[3]:
        print("Two pairs: " + str(hand))
        return True
    elif hand[0] == hand[1] and hand[3] == hand[4]:
        print("Two pairs: " + str(hand))
        return True
    elif hand[1] == hand[2] and hand[3] == hand[4]:
        print("Two pairs: " + str(hand))
        return True

def checkOnePair(hand):
    hand.sort()
    if hand[0] == hand[1]:
        print("One pair: " + str(hand))
        return True
    elif hand[1] == hand[2]:
        print("One pair: " + str(hand))
        return True
    elif hand[2] == hand[3]:
        print("One pair: " + str(hand))
        return True
    elif hand[3] == hand[4]:
        print("One pair: " + str(hand))
        return True

def checkHighCard(hand):
    hand.sort()
    print("High card: " + str(hand))

card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

data = getData()
max_rank = len(data)
results = []
print(max_rank)
for index, hand in enumerate(data):
    char_arr = []
    for char in hand[0]:
        char_arr.append(char)
    print("Hand", hand)
    print(char_arr)
    print("Index:", index)
    if not checkFiveOfAKind(char_arr):
        if not checkFourOfAKind(char_arr):
            if not checkFullHouse(char_arr):
                if not checkThreeOfAKind(char_arr):
                    if not checkTwoPairs(char_arr):
                        if not checkOnePair(char_arr):
                            if checkHighCard(char_arr):
                                results.append([1, hand[1], hand[0]])
                        else:
                            results.append([2, hand[1], hand[0]])
                    else:
                        results.append([3, hand[1], hand[0]])
                else:
                    results.append([4, hand[1], hand[0]])
            else:
                results.append([5, hand[1], hand[0]])
        else:
            results.append([6, hand[1], hand[0]])
    else:
        results.append([7, hand[1], hand[0]])

sorted_results = sorted(results, key=lambda x: x[0])
print(sorted_results)


for index, res in enumerate(sorted_results):
    if index < len(sorted_results) - 1:
        if res[0] == sorted_results[index + 1][0]:
            hand1 = res[2]
            hand2 = sorted_results[index + 1][2]
            print("Hand 1:", hand1, "Hand 2:", hand2)
            for index, cahr in enumerate(hand1):
                if card_value.index(hand1[index]) > card_value.index(hand2[index]):
                    print("Hand 1 wins")
                    print("switching...")
                    sorted_results[index], sorted_results[index + 1] = sorted_results[index + 1], sorted_results[index]
                    print(sorted_results)
                    break
                elif card_value.index(hand1[index]) < card_value.index(hand2[index]):
                    print("Hand 2 wins")
                    break
                else:
                    continue

print(sorted_results)

sum = 0

for index, res in enumerate(sorted_results):
    sum += (index + 1) * int(res[1])

print(sum)
