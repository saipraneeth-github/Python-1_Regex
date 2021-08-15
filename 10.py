d1 = {1:4, 2:5, 3:9, 4: 8}
d2 = {2:5, 4:8, 6:10, 8:15}

d3 = {}

union = dict(d1.items() | d2.items())
intersection = dict(d1.items() & d2.items())
print (union)
print(intersection)

d3 = dict(union.items() ^ intersection.items())

print(d3)
