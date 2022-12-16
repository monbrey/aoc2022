import sys
z=[('A','B'),('B','C'),('C','A')]
s=lambda x:ord(x)-64
r=lambda o,y:3 if o==y else 6 if (o,y) in z else 0
a=[[l[0],chr(ord(l[2])-23)]for l in open(sys.argv[1],'r')]
print(sum([s(t[1])+r(t[0],t[1])for t in a]))
w=lambda x:[y for y in z if y[0]==x][0][1]
l=lambda x:[y for y in z if y[1]==x][0][0]
c=lambda o,g:l(o)if g=='A'else o if g=='B'else w(o)
print(sum([s(c(t[0],t[1]))+r(t[0],c(t[0],t[1]))for t in a]))