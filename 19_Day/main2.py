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

def main_rule(string):
	starts_42 = re.compile("^("+rules[42]+")")
	starts_31 = re.compile("^("+rules[31]+")")

	count_42 =0
	while bool(starts_42.match(string)):
		match = starts_42.match(string)
		string = string[match.end():]
		count_42+=1

	count_31 =0
	while bool(starts_31.match(string)):
		match = starts_31.match(string)
		string = string[match.end():]
		count_31+=1

	return( count_31>=1 and count_42>count_31 and len(string)==0)

print(sum([main_rule(message) for message in messages]))