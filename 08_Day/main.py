inp = [line.rstrip() for line in open("input.txt").read().splitlines()]

def terminates(input):
	pc=0
	glob=0
	executed=[False] * len(input)

	while True:
		if pc>=len(input):
			break
		if executed[pc] or pc<0:
			print(glob)
			return False

		line = input[pc]
		inst = line[0:3]
		arg = int(line[3:])

		executed[pc]=True

		if inst == "acc":
			glob+=arg
		elif inst=="jmp":
			pc+=arg
			continue

		pc+=1

	print(glob)
	return True

terminates(inp)