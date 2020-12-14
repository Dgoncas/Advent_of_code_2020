from collections import defaultdict

input = [line.rstrip() for line in open("input.txt").read().splitlines()]

mask_1 = 0
mask_2 = 0

def change_mask(string):
	global mask_1
	global mask_2
	mask_1 = int("".join([('0' if x=='X' else x) for x in string]),2) #OR
	mask_2 = int("".join([('1' if x=='X' else x) for x in string]),2) #AND

mem = defaultdict(lambda x:0)

for inst in input:
	if "mask" in inst:
		change_mask(inst[7:])
	else:
		address = int(inst.split("[")[1].split("]")[0])
		value = int(inst.split("=")[1][1:])
		value = value | mask_1
		value = value & mask_2
		mem[address] = value
		
print(sum([mem[k] for k in mem.keys()]))