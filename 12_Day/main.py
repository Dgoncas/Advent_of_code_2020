input = [line.rstrip() for line in open("input.txt").read().splitlines()]

compass={'N':(0,-1),'S':(0,1),"W":(-1,0),"E":(1,0)}
turning={'L': (lambda xy: (xy[1],-xy[0]) ) ,'R': (lambda xy: (-xy[1],xy[0]) ) }

facing =(1,0)
position = (0,0)

for i in input:
	ins=i[0]
	val=int(i[1:])

	if ins in compass.keys():
		direction=compass[ins]
		position=(position[0]+direction[0]*val,position[1]+direction[1]*val)
	elif ins in turning.keys():
		for i in range(0,int(val/90)):
			facing=turning[ins](facing)
	else:
		position=(position[0]+facing[0]*val,position[1]+facing[1]*val)


print(abs(position[0])+abs(position[1]))




