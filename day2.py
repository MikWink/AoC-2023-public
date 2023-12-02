data = open("day2_data.txt", "r")

redDices = 12
greenDices = 13
blueDices = 14
sum = 0

for line in data:
    neededRed = 0
    neededGreen = 0
    neededBlue = 0
    possible = True

    gameIndex = int(''.join(filter(str.isdigit, line[5:8])))
    if gameIndex < 100:
        games = line[8:].rsplit(";")
    else:
        games = line[9:].rsplit(";")
    gameIndexBetter = ''.join(filter(str.isdigit, line[5:7]))

    print("GameIndex:", gameIndex, "Played Game:", games)

    for game in games:
        redDices = 12
        greenDices = 13
        blueDices = 14
        #print(game)
        dices = game.rsplit(",")
        for dice in dices:
            strippedDice = dice.strip()
            #print(strippedDice)
            if strippedDice.find("red") >= 0:
                redDices = redDices - int(strippedDice[0:2])
                if neededRed < int(strippedDice[0:2]):
                    neededRed = int(strippedDice[0:2])
            elif strippedDice.find("green") >= 0:
                #print(strippedDice)
                greenDices = greenDices - int(strippedDice[0:2])
                #print("Green Dices:", int(strippedDice[0:2]))
                if neededGreen < int(strippedDice[0:2]):
                    neededGreen = int(strippedDice[0:2])
            elif strippedDice.find("blue") >= 0:
                blueDices = blueDices - int(strippedDice[0:2])
                if neededBlue < int(strippedDice[0:2]):
                    neededBlue = int(strippedDice[0:2])
            #print("Red:", redDices, "Green:", greenDices, "Blue:", blueDices)

        if redDices < 0 or greenDices < 0 or blueDices < 0:
            possible = False
            print("Game is not Possible, needed Red", neededRed, "needed Green", neededGreen, "needed Blue", neededBlue, "power of Game", neededBlue*neededRed*neededGreen)

            print()



    powerOfGame = neededRed * neededGreen * neededBlue
    #print("trying to add")
    if possible:
        print("Game possible, power of Game:", powerOfGame)
        print("Added:", powerOfGame)
        sum = sum + powerOfGame
        print(sum)
    elif not possible:
        print("Game not possible, power of Game:", powerOfGame)
        sum = sum + powerOfGame
        print(sum)



print("Puzzle solution:", sum)