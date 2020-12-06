
input = [line.rstrip() for line in open("input.txt").read().splitlines()]
input.append("")

ans=0
dict={}

for person in input:
	if person=="":
		ans+=len(dict.keys())	
		dict={}
		continue
	for a in person:
		dict[a]=1

print(ans)

