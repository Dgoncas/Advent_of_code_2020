input = [int(char+"") for char in open("input.txt").read()]

def remove(first,number):
	global input
	for i in range(first,first+number):
		input[(i)%len(input)] = -1
	input = [i for i in input if i!=-1]

def get(first,number):
	res = []
	for i in range(first,first+number):
		res.append(input[(i)%len(input)])
	return res

def put(place,numbers):
	global current
	for n in numbers:
		input.insert(place,n)
		place += 1

def getList():
	first = input.index(1)
	for index in range(first+1,first+9):
		print(input[index%len(input)],end="")
	print()


size = len(input)
current_index = 0
current = input[0]

for move in range(100):

	print(input)
	destination_label = input[current_index]-1
	destination = -1

	pickup = get(current_index+1,3)
	remove(current_index+1,3)

	current_index = input.index(current)

	while True:
		if destination_label in input:
			destination = input.index(destination_label)
			break
		destination_label -= 1
		if destination_label<0:
			destination_label += size+1

	put((destination+1)%len(input),pickup)

	current_index = input.index(current)

	current_index += 1
	current_index %= len(input)
	current = input[current_index]

print(input)
getList()