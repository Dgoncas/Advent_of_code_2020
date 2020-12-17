input = [line.rstrip() for line in open("input.txt").read().splitlines()]

moves = {(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(1,1,0),(-1,-1,0),(-1,1,0),(1,-1,0),
	(1,0,1),(-1,0,1),(0,0,1),(0,1,1),(0,-1,1),(1,1,1),(-1,-1,1),(-1,1,1),(1,-1,1),
	(1,0,-1),(-1,0,-1),(0,0,-1),(0,1,-1),(0,-1,-1),(1,1,-1),(-1,-1,-1),(-1,1,-1),(1,-1,-1)}

cubes = set()
tempCubes = set()

corner_1 = [-1,-1,-1]
corner_2 = [len(input[0]),len(input),1]

def checkCubes(cube):
	active = 0
	inactive = 0
	for m in moves:
		if (cube[0]+m[0], cube[1]+m[1], cube[2]+m[2]) in cubes:
			active += 1
		else:
			inactive += 1
	return {"active":active,"inactive":inactive}

def exploreCubes(cube):
	result = checkCubes(cube)
	if (cube in cubes) and (not(result["active"]==2 or result["active"]==3)):
		tempCubes.remove(cube)
	if (not (cube in cubes)) and (result["active"] == 3):
		tempCubes.add(cube)

for y in range(len(input)):
	for x in range(len(input[0])):
		if input[y][x]=='#':
			cubes.add((x,y,0))

#BOOT CYCLE LOOP
for i in range(6):
	
	tempCubes = cubes.copy()
	for z in range(corner_1[2],corner_2[2]+1):
		for y in range(corner_1[1],corner_2[1]+1):
			for x in range(corner_1[0],corner_2[0]+1):
				exploreCubes((x,y,z))
	cubes = tempCubes

	for cube in cubes:
		if cube[0]<=corner_1[0]:
			corner_1[0] =cube[0]-1
		if cube[1]<=corner_1[1]:
			corner_1[1] =cube[1]-1
		if cube[2]<=corner_1[2]:
			corner_1[2] =cube[2]-1

		if cube[0]>=corner_2[0]:
			corner_2[0]=cube[0]+1
		if cube[1]>=corner_2[1]:
			corner_2[1]=cube[1]+1
		if cube[2]>=corner_2[2]:
			corner_2[2]=cube[2]+1

print(len(cubes))