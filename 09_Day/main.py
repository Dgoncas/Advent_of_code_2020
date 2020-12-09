input = [int(line.rstrip()) for line in open("input.txt").read().splitlines()]

preamble=25
prev = [input[i] for i in range(0,preamble)]
def next(n):
	found=any([(abs(p-n) in prev) for p in prev])
	prev.pop(0)
	prev.append(n)
	return found

number=[input[l] for l in range(preamble,len(input)) if not next(input[l])]
number=number[0]

print("NUMBER :"+str(number))