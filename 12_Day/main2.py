input = [line.rstrip() for line in open("input.txt").read().splitlines()]

compass={'N':(0,-1),'S':(0,1),"W":(-1,0),"E":(1,0)}
turning={'L': (lambda xy: (xy[1],-xy[0]) ) ,'R': (lambda xy: (-xy[1],xy[0]) ) }

facing =(1,0)
position = (10,-1)

origin=(0,0)

for i in input:
	ins=i[0]
	val=int(i[1:])

	if ins in compass.keys():
		direction=compass[ins]
		position=(position[0]+direction[0]*val,position[1]+direction[1]*val)
	elif ins in turning.keys():
		for i in range(0,int(val/90)):
			position=turning[ins](position)
	else:
		origin=(origin[0]+position[0]*val,origin[1]+position[1]*val)

print(abs(origin[0])+abs(origin[1]))




