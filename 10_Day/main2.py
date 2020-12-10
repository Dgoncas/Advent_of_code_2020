from collections import defaultdict
input = sorted([int(line.rstrip()) for line in open("input.txt")])
sols={input[-1]:1}

def sol(i):
	if i in sols:
		return sols[i]
	else:
		sols[i]=sum([(sol(j) if j in input else 0) for j in range(i+1,i+4)])
		return sols[i]

print(sol(0))