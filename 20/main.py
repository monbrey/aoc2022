import sys
from time import time

decryption = 811589153
# set each item with a boolean to determine if its been moved
input = open(sys.argv[1]).read().split('\n')
numbers = [(i,int(x)*decryption) for i,x in enumerate(input)]

for run in range(0,10):
	for i in range(len(numbers)):
		# find the next item, get its current index
		x = next(x for x in numbers if x[0] == i)
		idx = numbers.index(x)

		# remove it
		numbers.pop(idx)
		# calc the new index
		new_i = (idx+x[1]) % len(numbers)
		# and insert it - 0 wraps to the end
		if new_i == 0:
			numbers.append(x)
		else:
			numbers.insert(new_i, x)

	sorted_list = [x[1] for x in numbers]
	start = sorted_list.index(0)

print(sum([sorted_list[(start+1000)%len(sorted_list)],sorted_list[(start+2000)%len(sorted_list)],sorted_list[(start+3000)%len(sorted_list)]]))
print(time())
