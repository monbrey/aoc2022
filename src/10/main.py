import os
import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")

pp = pprint.PrettyPrinter(indent=2)

X = 1
cycle = 0
strengths = []

crt = ['','','','','','']


def inc():
	global cycle
	draw()
	cycle += 1
	if cycle == 20 or (cycle-20) % 40 == 0:
		strengths.append(cycle*X)



def draw():
	sprite_pos = range(X-1,X+2)
	row = (cycle/40)//1
	pos = cycle%40
	print(row,pos)
	crt[int(row)]+=('#' if pos in sprite_pos else ' ')


while input:
	line = input.readline().strip().split(' ')
	match line[0]:
		case 'noop':
			inc()
		case 'addx':
			inc()
			inc()
			X += int(line[1])
		case '': break

print(strengths)
print(sum(strengths))
print("\n".join(crt))