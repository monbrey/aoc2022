import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r").read()

grid = [line for line in input.split('\n')]

rows = len(grid)
cols = len(grid[0])
visible = 0

for i in range(0,rows):
	row = grid[i]
	# build the col for ease of use
	for j in range(0,cols):
		col = "".join([grid[i][j] for i in range(0,rows)])
		# handle edges
		if any(x in [0, rows-1, cols-1] for x in [i,j]):
			visible = visible + 1
			continue
		# get tree
		tree = grid[i][j]
		# check before it in row
		if max(row[:j]) < tree:
			visible += 1
			continue
		# check after it in row
		if max(row[j+1:]) < tree:
			visible += 1
			continue
		# check before it in column
		if max(col[:i]) < tree:
			visible += 1
			continue
		# check after it in column
		if max(col[i+1:]) < tree:
			visible += 1
			continue

# part 1
print(visible)

max_score = 0

def count_until_blocked(tree, view):
	sum = 0
	for x in view:
		sum += 1
		if x >= tree:
			return sum
	
	return sum

for i in range(0,rows):
	row = grid[i]
	for j in range(0,cols):
		curr_score = 1
		# build the col for ease of use
		col = "".join([grid[i][j] for i in range(0,rows)])
		# get tree
		tree = grid[i][j]
		# count before it in row
		curr_score *= count_until_blocked(tree, row[:j][::-1])
		# count after it in row
		curr_score *= count_until_blocked(tree, row[j+1:])
		# count before it in column
		curr_score *= count_until_blocked(tree, col[:i][::-1])
		# count after it in column
		curr_score *= count_until_blocked(tree, col[i+1:])

		if curr_score > max_score:
			max_score = curr_score

# part 2
print(max_score)

