import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Part 1


def common(b):
  # find the common item in each backpacks by splitting the compartments and
  a, b = b[:len(b) // 2], b[len(b) // 2:]
  return list(set(a) & set(b))[0]


def priority(x):
  # calculate the priority
  return ord(x) - 38 if x.isupper() else ord(x) - 96


backpacks = [b.rstrip() for b in open(f"{dir_path}/input.txt", "r")]


print(sum([priority(common(b.rstrip())) for b in backpacks]))


# Part 2
total = 0

for i in range(0, len(backpacks), 3):
  # get every three backpacks, find the common item, and add its priority to the total
  a, b, c = backpacks[i:i + 3]
  badge = list(set(a) & set(b) & set(c))[0]
  total += priority(badge)


print(total)
