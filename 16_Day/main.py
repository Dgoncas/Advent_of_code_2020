from numpy import product

input = [line.rstrip() for line in open("input.txt").read().split("\n\n")]

def validField(name,value):
    ranges = fields[name]
    return (value>=ranges[0][0] and value<=ranges[0][1]) or (value>=ranges[1][0] and value<=ranges[1][1])

fields = {}
for field in input[0].split("\n"):
    name = field.split(": ")[0]
    ranges = [ (int(range_.split("-")[0]),int(range_.split("-")[1])) for range_ in (field.split(": ")[1]).split(" or ")]
    fields[name] = ranges

nearTickets = input[2].split("\n")[1:]

ans = 0
for ticket in nearTickets:
    values = [int(value) for value in ticket.split(",")]
    for value in values:
        if not (any([validField(field,value )for field in fields.keys()])):
            ans += value
            break

print(ans)