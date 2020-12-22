input = [line for line in open("input.txt").read().split("\n\n")]

players = [[int(card) for card in player.split("\n") if not "Player" in card]for player in input]

while len(players[0])>0 and len(players[1])>0:
	bigger = 0 if players[0][0] > players[1][0] else 1
	players[bigger].append(players[bigger][0])
	players[bigger].append(players[not bigger][0])

	players[0].pop(0)
	players[1].pop(0)
	print(players)

print(sum([(players[0][index]*(len(players[0])-index))for index in range(len(players[0]))]))
print(sum([(players[1][index]*(len(players[1])-index))for index in range(len(players[1]))]))