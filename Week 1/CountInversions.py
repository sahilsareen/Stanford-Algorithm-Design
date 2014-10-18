import sys, bisect

a = map(int,open(sys.argv[1]))
b = sorted(a)
r = 0
for d in a:
    p = bisect.bisect_left(b,d)
    r += p
    b.pop(p)
print r 
