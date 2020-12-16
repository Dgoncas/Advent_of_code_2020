from numpy import product

input = [line.rstrip() for line in open("input.txt").read().split("\n\n")]

def validField(name,value):
	ranges = fields[name]
	return (value>=ranges[0][0] and value<=ranges[0][1]) or (value>=ranges[1][0] and value<=ranges[1][1])

def areAllValid(name,values):
	return all(list(map(lambda x: validField(name,x),values)))

fields = {}
for field in input[0].split("\n"):
	name = field.split(": ")[0]
	ranges = [ (int(range_.split("-")[0]),int(range_.split("-")[1])) for range_ in (field.split(": ")[1]).split(" or ")]
	fields[name] = ranges

myTicket = input[1].split("\n")[1]
nearTickets = input[2].split("\n")[1:]
tickets = [[] for _ in range(len(fields))]

for ticket in nearTickets:
	values = [int(value) for value in ticket.split(",")]
	skip=False
	for value in values:
		if not (any([validField(field,value )for field in fields.keys()])):
			skip=True
			break
	if(skip):
		continue
	for index in range(len(fields)):
		tickets[index].append(values[index])

possible_fields = [[field for field in fields.keys() if areAllValid(field,values)] for values in tickets]
print(possible_fields)
definitive_fields = [None for _ in range(len(fields))]

while None in definitive_fields:
	for index in range(len(possible_fields)):
		field = possible_fields[index]
		if len(field)==1:
			delete = field[0]
			definitive_fields[index] = delete
			for index2 in range(len(possible_fields)):
				if delete in possible_fields[index2]:
					possible_fields[index2].remove(delete)

myTicket = [int(value) for value in myTicket.split(",")]
print(product([myTicket[index] for index in range(len(fields)) if ("departure" in definitive_fields[index])]) )