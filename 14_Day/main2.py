from collections import defaultdict

input = [line.rstrip() for line in open("input.txt").read().splitlines()]

mask = []

def apply_mask(address):
	addresses = [""]
	base_mask = ""
	binary_address = bin(address)[2:]
	binary_address = "0"*(36-len(binary_address))+binary_address
	for bit in range(0,36):
		base_mask+= (binary_address[bit] if mask[bit] == '0' else mask[bit])

	for bit in base_mask:
		add2 = []
		for address in addresses:
			if bit != 'X':
				add2.append(address+bit)
			else:
				add2.append(address+'1')
				add2.append(address+'0')
		addresses = add2.copy()

	addresses = [int(x,2) for x in addresses]
	return addresses

mem = defaultdict(lambda x:0)

for inst in input:
	if "mask" in inst:
		mask = inst[7:]
	else:
		address = int(inst.split("[")[1].split("]")[0])
		value = int(inst.split("=")[1][1:])

		masked_addresses = apply_mask(address)
		for masked_address in masked_addresses:
			mem[masked_address] = value

print(sum([mem[k] for k in mem.keys()]))