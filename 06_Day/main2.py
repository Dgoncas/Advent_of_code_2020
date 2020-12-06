
input = [line.rstrip() for line in open("input.txt").read().splitlines()]
input.append("")

ans=0
dict={}

people=0

for person in input:
	if person=="":
		for d in dict.keys():
			if dict[d]==people:
				ans+=1
		dict={}
		people=0
		continue
	people+=1
	for a in person:
		if not a in dict.keys():
			dict[a]=0
		dict[a]+=1

print(ans)

