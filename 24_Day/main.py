from copy import deepcopy

input = open("input.txt").read()

directions = [(1,0),(-1,0),(0.5,0.5),(-0.5,0.5),(0.5,-0.5),(-0.5,-0.5)]

input = input.replace("se","2,")
input = input.replace("sw","3,")
input = input.replace("ne","4,")
input = input.replace("nw","5,")
input = input.replace("e","0,")
input = input.replace("w","1,")

input = input.split("\n")
input = [l.split(",") for l in input]
input = [ [int(x) for x in l if x != ''] for l in input]

fliped = set()
fliped.add((0.0,0.0))

counter = 0

for line in input:
	position = [0,0]
	for instruction in line:
		move = directions[instruction]
		position[0] = position[0]+move[0]
		position[1] = position[1]+move[1]
	tup = (float(position[0]),float(position[1]))
	if tup in fliped:
		fliped.remove(tup)
	else:
		fliped.add(tup)

print(len(fliped))