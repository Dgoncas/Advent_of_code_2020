from collections import defaultdict

input = [line for line in open("input.txt").read().splitlines()]

all_ingredients = set()
all_allergens = set()

posible_ingredients = defaultdict(lambda : -1)

for food in input:
	ingredients = food.split(" (contains ")[0].split(" ")
	allergens = food.split(" (contains ")[1][:-1].split(", ")

	all_ingredients = all_ingredients.union(ingredients)
	all_allergens = all_allergens.union(allergens)

	for allergen in allergens:
		if posible_ingredients[allergen] == -1:
			posible_ingredients[allergen] = set(ingredients)
		else:
			posible_ingredients[allergen] = posible_ingredients[allergen].intersection(set(ingredients))

ingredients_with_allergens = set()
for k in posible_ingredients.keys():
	ingredients_with_allergens = ingredients_with_allergens.union(posible_ingredients[k])
ingredients_without_allergens = all_ingredients-ingredients_with_allergens

while True:
	done = True
	for allergen in posible_ingredients.keys():
		ingredient = posible_ingredients[allergen]
		if len(ingredient) == 1:
			ingredient = list(ingredient)[0]
			for allergen2 in posible_ingredients.keys():
				if allergen2!=allergen and (ingredient in posible_ingredients[allergen2]):
					posible_ingredients[allergen2].remove(ingredient)
					done = False
	if done:
		break

ordered = list(posible_ingredients.keys())
ordered.sort()
for k in ordered:
	print(list(posible_ingredients[k])[0],end="")
	if k!= ordered[-1]:
		print(",",end="")
print()