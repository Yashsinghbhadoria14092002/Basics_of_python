# tuples and strings are immutable but list can be changed
t = (3, 5, 23, 23)
print(t.count(5))
print(t.index(3))
# t[0] = 89 # Tuple is immutable and hence this line throws an error