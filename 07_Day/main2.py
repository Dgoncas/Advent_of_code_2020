input = [line for line in open("input.txt").read().splitlines()]

bags = {}

for l in input:
	l2=l.split("contain")
	b1=l2[0].split(" ")[0]+" "+l2[0].split(" ")[1]
	bags[b1]= [( int(b.split(" ")[1]), " ".join(b.split(" ")[2:-1]) ) for b in l2[1].split(",") if b!=" no other bags."]

def dfs(bag,parent):
	total=0
	for b2 in bags[bag]:
		total+= (b2[0]+ (b2[0] * dfs(b2[1],bag)))
	return total

print(dfs("shiny gold",""))