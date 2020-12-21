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

while any([(len(v)-1) for k,v in possibly_contained.items()]):
	for k,v in possibly_contained.items():
		if len(v)==1:
			for k2,v2 in possibly_contained.items():
				if k2 != k:
					possibly_contained[k2] = {i for i in v2 if not i in v}

print(",".join([list(possibly_contained[k])[0] for k in sorted(possibly_contained.keys())]))