input = [line for line in open("input.txt").read().splitlines()]

def computeOperations(string):
	string=string.split(" ")
	while '+' in string:
		for index in range(len(string)):
			if string[index]=='+':
				n1 = int(string[index-1])
				n2 = int(string[index+1])
				result = n1+n2
				string=string[:index-1]+(string[index+2:])
				string.insert(index-1,str(result))
				break

	while len(string) != 1:
		n1 = int(string[0])
		n2 = int(string[2])
		result = n1*n2
		string=string[3:]
		string.insert(0,str(result))
	return string[0]


def computeParentesis(string):
	last_open = -1
	last_close = -1
	for index in range(len(string)):
		if string[index] == '(':
			last_open = index
		if string[index] == ')':
			last_close = index
			break
	if last_open == -1:
		return None
	return string[0:last_open] + computeOperations(string[last_open+1:last_close]) + string[last_close+1:]

def computeExpresion(string):
	while True:
		step = computeParentesis(string)
		if step == None:
			break
		else:
			string=step

	return computeOperations(string)

ans = sum([int(computeExpresion(expresion)) for expresion in input])
print(ans)