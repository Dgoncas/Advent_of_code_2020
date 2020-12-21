input = [line for line in open("input.txt").read().splitlines()]

all_ingredients = set()

possibly_contained = {}

for food in input:
	ingredients, allergens = food[:-1].split(" (contains ")
	ingredients = ingredients.split(" ")
	allergens = allergens.split(", ")

	all_ingredients.update(ingredients)

	for allergen in allergens:
		if not allergen in possibly_contained:
			possibly_contained[allergen] = set(ingredients)
		else:
			possibly_contained[allergen] = possibly_contained[allergen].intersection(set(ingredients))

safe_ingredients = all_ingredients
for (k,v) in possibly_contained.items():
	safe_ingredients -= v

print(sum([sum([(item in safe_ingredients)for item in food.split(" ")]) for food in input]))