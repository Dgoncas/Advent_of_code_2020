from numpy import prod

input = open("input.txt").read().splitlines()[1].split(",")

buses = [(int(input[index]),index) for index in range(0,len(input)) if input[index]!='x']

#  x%mod = mod    HAS TO HE TRUE FOR EVERY BUS -> chinese remainder theorem
mods = [x for (x,y) in buses]
mods_result = [(x-y)%x for (x,y) in buses]

def chineseRemainer(m,m_r):
	N=prod(m)
	resut=0
	for index in range(0,len(m)):
		ni=int(N/m[index])
		xi=modularInverse(ni,m[index])
		resut+=m_r[index]*ni*xi
	return resut%N

# find X such as  (X*num)%mod=1
def modularInverse(num,mod):
	for i in range(1,mod+1):
		if (num*i)%mod==1:
			return i

print(chineseRemainer(mods,mods_result))