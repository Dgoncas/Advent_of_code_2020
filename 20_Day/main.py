from numpy import product
from collections import defaultdict

input  = [tile for tile in open("input.txt").read().split("\n\n")]

tiles = defaultdict(lambda: [])
sides = defaultdict(lambda: [])
neigh = defaultdict(lambda: [])

for tile in input:
	id = -1
	for line in tile.splitlines():
		if "Tile" in line:
			id = int(line.split(" ")[1][:-1])
		else:
			tiles[id].append(line)

for id in tiles.keys():
	tile = tiles[id]
	sides[id].append(tile[0])
	sides[id].append(tile[-1])
	left =[]
	rigth =[]
	for line in tile:
		left.append(line[0])
		rigth.append(line[-1])
	left = "".join(left)
	rigth = "".join(rigth)
	sides[id].append(left)
	sides[id].append(rigth)

for tile_1 in tiles.keys():
	for tile_2 in tiles.keys():
		for side in sides[tile_1]:
			if tile_1==tile_2:
				break
			if (side in sides[tile_2]) or ("".join(list(reversed(side))) in sides[tile_2]):
				neigh[tile_1].append(tile_2)

print(product([key for key in tiles.keys() if len(neigh[key])==2]))