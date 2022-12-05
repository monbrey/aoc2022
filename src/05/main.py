# Part 1
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")

# I didnt want to read this from file
stacks = [
    ['W', 'D', 'G', 'B', 'H', 'R', 'V'],
    ['J', 'N', 'G', 'C', 'R', 'F'],
    ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
    ['J', 'D', 'S', 'V'],
    ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
    ['P', 'G', 'H', 'C', 'M'],
    ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
    ['S', 'J', 'R'],
    ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']
]

moves = [re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
         for line in input]

# for move in moves:
#   num, source, dest = int(move[0]), int(move[1]) - 1, int(move[2]) - 1
#   for i in range(0, num):
#     stacks[dest].append(stacks[source].pop())

# print(''.join([stack[-1] for stack in stacks]))

# Part 2
# commented out previous moves as they were modifying the state of the stacks, need to start fresh

for move in moves:
  num, source, dest = int(move[0]), int(move[1]) - 1, int(move[2]) - 1
  stacks[dest].extend(stacks[source][-num:])
  stacks[source] = stacks[source][0:-num]

print(''.join([stack[-1] for stack in stacks]))
