def getTimesAndDist():
    data = open("day6_data.txt", "r")

    times = []
    dist = []

    for line in data:
        if not times:
            times = line.split()[1:]
        else:
            dist = line.split()[1:]

    return times, dist

def getOneTimeAndDist():
    times, dist = getTimesAndDist()
    time = ""
    distance = ""
    for t in times:
        time += t
    for d in dist:
        distance += d
    return int(time), int(distance)



def calculateWins(time, dist):
    win_counter = 0
    for sec in range(time):
        speed = sec
        distance = speed * (time - sec)
        #print("Index:", index, "Time:", time, "Dist:", dist, "Speed:", speed, "Distance:", distance)
        if distance > dist:
            win_counter += 1

    return win_counter

def part1():
    times, dist = getTimesAndDist()
    factor = 1
    wins = 1
    for index, time in enumerate(times):
        factor = calculateWins(int(time), int(dist[index]))
        #print("Zwischenergebnis wins:", wins, "times:", factor)
        wins *= factor
    return wins

def part2():
    time, dist = getOneTimeAndDist()
    return calculateWins(time, dist)



print(part1())
print(part2())