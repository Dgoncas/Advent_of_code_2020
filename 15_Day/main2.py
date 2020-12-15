from collections import defaultdict

input = [int(line) for line in open("input.txt").read().split(",")]

seen_numbers = defaultdict(lambda: [])

turn = 1
prev_number = 0

while True:

	if len(input)==0:
		if len(seen_numbers[prev_number])==1:
			seen_numbers[0].append(turn)
			prev_number=0
		else:
			number = turn-1-seen_numbers[prev_number][-2]
			seen_numbers[number].append(turn)
			prev_number=number
	else:
		number = input.pop(0)
		seen_numbers[number].append(turn)
		prev_number = number

	if turn == 30000000:
		break

	turn+=1

print(prev_number)