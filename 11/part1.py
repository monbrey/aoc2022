import os
import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
pp = pprint.PrettyPrinter(indent=2)

input = [turn.split('\n') for turn in open(f"{dir_path}/input.txt", "r").read().split('\n\n')]
monkeys = []


def prepare():
	for i, turn in enumerate(input):
		items = [int(x) for x in turn[1][18:].split(', ')]
		op = turn[2].split(' = ')[1].split(' ')[1:]
		test = (int(turn[3].split(' ')[-1]), int(turn[4].split(' ')[-1]), int(turn[5].split(' ')[-1]))
		monkeys.append({ 'items': items, 'op': op, 'test': test, 'count': 0 })



def calculate(l, op):
	r = l if op[1] == 'old' else int(op[1])
	match op[0]:
		case '+': return int((l + r) // 3)
		case '*': return int((l * r) // 3)


def round():
	for monkey in monkeys:
		for j in range(0, len(monkey['items'])):
			item = monkey['items'].pop()
			item = calculate(item, monkey['op'])
			target = monkeys[monkey['test'][1] if (item % monkey['test'][0]) == 0 else monkey['test'][2]]
			target['items'].append(item)
			monkey['count'] += 1


prepare()
for _ in range(0,20):
	round()


counts = sorted([m['count'] for m in monkeys])
print(counts[-1] * counts[-2])
