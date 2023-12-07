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


data = getData()
for hand in data:
    char_arr = []
    for char in hand[0]:
        char_arr.append(char)
    print(char_arr)
    if not checkFiveOfAKind(char_arr):
        if not checkFourOfAKind(char_arr):
            if not checkFullHouse(char_arr):
                if not checkThreeOfAKind(char_arr):
                    if not checkTwoPairs(char_arr):
                        if not checkOnePair(char_arr):
                            checkHighCard(char_arr)