# Part 1
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")

stacks = None
stacks_parsed = False
items = []

for line in input:
  if len(line.strip()) == 0:
    break
  elif stacks_parsed == False:
    items = [line[i:i+4].strip() for i in range(0,len(line),4)]
    if stacks == None:
      stacks = [None] * len(items)
    for i in range(0,len(items)):
      if len(items[i]) == 0 or items[i][0] != '[':
        continue
      if stacks[i] == None:
        stacks[i] = []
      stacks[i].insert(0,items[i][1])

moves = [re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
         for line in input]

for move in moves:
  num, source, dest = int(move[0]), int(move[1]) - 1, int(move[2]) - 1
  stacks[dest].extend(stacks[source][-num:])
  stacks[source] = stacks[source][0:-num]

print(''.join([stack[-1] for stack in stacks]))
