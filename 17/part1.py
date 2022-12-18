import sys

ROCKS = [
  [(2, 0), (3, 0), (4, 0), (5, 0)], # ____
  [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)], # +
  [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)], # __|
  [(2, 0), (2, 1), (2, 2), (2, 3)], # |
  [(2, 0), (2, 1), (3, 0), (3, 1)], # #
]

MOVEMENTS = open(sys.argv[1]).read().strip()

TOWERS = {(x,0) for x in range(7)}

# movement counter
mc = 0

print(len(MOVEMENTS))
for r in range(1_000_000_000_000):
  if mc%len(MOVEMENTS) == 0 and r%5 == 0: print(r)
  # grab a rock and offset it by max height + 4
  h = max(y for x,y in TOWERS)
  rock = [(x,y+h+4) for x,y in ROCKS[r%5]]

  while True:
    m = MOVEMENTS[mc%len(MOVEMENTS)]
    mc += 1
    dx = -1 if m == '<' else +1

    # get the new horizontal position
    new_pos = [(x+dx,y) for x,y in rock]
    # check collisions with walls
    if any(x < 0 or x >= 7 for x,y in new_pos):
      new_pos = rock
    # check collisions with towers
    elif any(piece in TOWERS for piece in new_pos):
      new_pos = rock
    # no collisions, the rock moves
    rock = new_pos
    # now check the lowered position
    new_pos = [(x,y-1) for x,y in rock]
    if any(piece in TOWERS for piece in new_pos):
      # cant move down, it settled
      TOWERS.update(rock)
      break
      
    # no collision, rock moves down
    rock = new_pos

print(max(y for x,y in TOWERS))