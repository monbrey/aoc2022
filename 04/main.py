# Part 1

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


def splitter(x):
  # split and cast each line into two sets of ints
  return list(
      map(lambda x: list(
          map(lambda x: int(x), x.split('-'))
      ), x.rstrip().split(','))
  )


def contained(a, b):
  # check if the limits of one range fully contain the other
  return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])


ranges = [splitter(line) for line in open(f"{dir_path}/input.txt", "r")]
print(sum(1 if contained(a, b) else 0 for a, b in ranges))


# Part 2


def overlap(a, b):
  # check if there is any intersection between the ranges
  # add the +1 to make the ranges last-digit inclusive
  return len(set(range(a[0], a[1] + 1)) & set(range(b[0], b[1] + 1))) > 0


print(sum(1 if overlap(a, b) else 0 for a, b in ranges))
