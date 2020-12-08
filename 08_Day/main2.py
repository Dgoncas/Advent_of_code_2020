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

for index in range(0,len(inp)):
	if inp[index][0:3] == "jmp" or inp[index][0:3]=="nop":
		in2=inp.copy();
		if inp[index][0:3] =="jmp":
			in2[index]="nop"+in2[index][3:]
		elif inp[index][0:3]=="nop":
			in2[index]="jmp"+in2[index][3:]
		if terminates(in2):
			break
