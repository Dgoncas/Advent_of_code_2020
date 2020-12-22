from copy import deepcopy

input = [line for line in open("input.txt").read().split("\n\n")]

players = [[int(card) for card in player.split("\n") if not "Player" in card]for player in input]

def game(pls,configurations):
	pls2 = deepcopy(pls)
	while True:

		if len(pls2[0]) == 0:
			return (1,pls2[1])
		if len(pls2[1])== 0:
			return (0,pls2[0])

		if pls2 in configurations:
			return (1,pls2[1])
		configurations.append(deepcopy(pls2))

		winner = 0
		card0 = pls2[0].pop(0)
		card1 = pls2[1].pop(0)

		if(len(pls2[1])>=card1 and len(pls2[0])>=card0):
			winner = game([pls2[0][:card0].copy(),pls2[1][:card1].copy()],[])[0]
		else:
			winner = 0 if card0>card1 else 1

		pls2[winner].append(card0 if winner==0 else card1)
		pls2[winner].append(card1 if winner==0 else card0)

winner_deck=game(players,[])[1]
print(sum([winner_deck[index]*(len(winner_deck)-index)for index in range(len(winner_deck))]))
