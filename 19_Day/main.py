import re

input = [line for line in open("input.txt").read().split("\n\n")]

rules = {int(rule.split(": ")[0]):rule.split(": ")[1] for rule in input[0].splitlines()}
messages = input[1].splitlines()

keys = list(rules.keys())
keys.sort()

for i in reversed(keys):
	rules[i] = rules[i].replace("\"","")
	if " " in rules[i] or "|" in rules[i]:
		rules[i] = "("+rules[i]+")"
	for j in reversed(keys):
		rules[j] = rules[j].replace(str(i),rules[i])

rules = {k:rules[k].replace(" ","") for k in rules.keys()}
expresion = re.compile("^"+rules[0]+"$")

print(sum([bool(expresion.match(message)) for message in messages]))