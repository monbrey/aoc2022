import sys
s=sorted([sum(map(int,e.split('\n')))for e in open(sys.argv[1]).read().split('\n\n')])
print(s[-1],sum(s[-3:]))