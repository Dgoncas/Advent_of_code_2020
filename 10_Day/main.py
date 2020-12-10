input = [int(line) for line in open("input.txt").read().splitlines()]

input.sort()

jolts=0
diferences=[]

for index in range(0,len(input)):
	if(abs(jolts-input[0])<=3):
		diferences.append(abs(jolts-input[0]))
		jolts=input[0]
		input.pop(0)
jolts+=3;
diferences.append(3);

print(jolts)
print(diferences.count(1)*diferences.count(3))