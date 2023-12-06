data = open("day5_data.txt", "r").read().split("\n\n")
seeds = [int(i) for i in data[0][7:].split(" ")]
mappings = [[[int(i)for i in line.split(" ")]for line in mapping.splitlines()[1:]] for mapping in data[1:]]






