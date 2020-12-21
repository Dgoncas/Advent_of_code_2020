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

ans = 0
for food in input:
	ingredients = food.split(" (contains ")[0].split(" ")
	for ingredient in ingredients:
		if ingredient in ingredients_without_allergens:
			ans += 1
print(ans)