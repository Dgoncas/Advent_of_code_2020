from collections import defaultdict

input = [list(line.rstrip()) for line in open("input.txt").read().splitlines()]
seats=defaultdict(lambda:0)
moves=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

for y in range(0,len(input)):
	for x in range(0,len(input[0])):
		if input[y][x]!='.':
			seats[(x,y)]=input[y][x]=='L'

def inBounds(coord):
	return coord[0]>=0 and coord[1]>=0 and coord[0]<len(input[0]) and coord[1]<len(input)

def read(coord):
	em=0
	oc=0
	for m in moves:
		new=(coord[0]+m[0],coord[1]+m[1])
		if new in seats.keys():
			oc+=seats[new]
			em+=not seats[new]
	return (em,oc)

while True:
	change=False
	seats2=seats.copy()
	for s in seats.keys():
		count=read(s)
		if seats[s]:
			if count[1]>=4:
				seats2[s]=0
				change=True
		else:
			if count[1]==0:
				seats2[s]=1
				change=True
	seats=seats2
	if not change:
		break

print(sum(seats[k] for k in seats.keys()))