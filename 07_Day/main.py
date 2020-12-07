input = [line for line in open("input.txt").read().splitlines()]

bags = {}

for l in input:
	l2=l.split("contain")
	b1=l2[0].split(" ")[0]+" "+l2[0].split(" ")[1]
	bags[b1]= [( int(b.split(" ")[1]), " ".join(b.split(" ")[2:-1]) ) for b in l2[1].split(",") if b!=" no other bags."]

def dfs(bag,parent):

	if(bag=="shiny gold" and parent!=""):
		return True

	for b2 in bags[bag]:
		if dfs(b2[1],bag): return True
	return False

ans=0
for k in bags.keys():
	if dfs(k,""):
		ans+=1
print(ans)