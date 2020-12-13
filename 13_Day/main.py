input = [line.rstrip() for line in open("input.txt").read().splitlines()]

time = int(input[0])
buses = [int(x) for x in input[1].split(',') if x!='x']

waitingTime = lambda bus: (bus-(time%bus))%bus

minimumWaiting=(waitingTime(buses[0]),buses[0])

for bus in buses:
	minimumWaiting= min(minimumWaiting,(waitingTime(bus),bus))

print(minimumWaiting[0]*minimumWaiting[1])
