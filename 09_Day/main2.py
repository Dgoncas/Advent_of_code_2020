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
keys=[]

for l in range(0,len(input)):
	sum=input[l]
	for r in range(l+1,len(input)):
		sum+=input[r]
		if sum==number:
			for i in range(l,r+1):
				keys.append(input[i])


print("KEYS :"+str(keys))
print("RESULT :"+str(min(keys)+max(keys)))