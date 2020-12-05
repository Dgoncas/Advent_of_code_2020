from termcolor import colored

input = [ line.rstrip() for line in open("input.txt").read().splitlines() ]

seats=[]
for i in range(0,128):
	seats.append([True]*8);
m=0

for pas in input:
	ur=127
	lr=0
	lc=0
	rc=7
	for letter in pas:
		if letter=="B":
			lr=(ur+lr+1)/2
		elif letter=="F":
			ur=(lr+ur+1)/2-1
		elif letter=="R":
			lc=(lc+rc+1)/2
		elif letter=="L":
			rc=(lc+rc+1)/2-1
	ur=int(ur)
	lr=int(lr)
	lc=int(lc)
	rc=int(rc)
	seats[ur][rc]=False

print()
for row in range(0,128):
	print("%4s" % (str(row))	,end="")
	for seat in range(0,8):
		if seats[row][seat]:
			print(colored("%7s"%(str(seats[row][seat])),"green"),end="")
		else:
			print(colored("%7s"%(str(seats[row][seat])),"red"),end="")

	print()
print()