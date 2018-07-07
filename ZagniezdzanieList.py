# 1. listy w liście

x = [1, 2, 3], [2, 5,  6] # lista 2 elementowa


a = [1, 2, 3] # to samo co wyżej
b = [4, 5, 6]

x = [a, b]
# spodziewamy się 3
print(x[0][2])
# spodziewamy się 2
print(len(x))

assert x[0][2] == 3
assert len(x) == 2

c = a
c.append(6)

assert a == [1, 2, 3, 6]
d = b.copy()
d.append(7)

print(x)
y = x.copy()
print(y)

assert not x is y
assert y[0]

y[0].append(7)

assert a == [1,2,3,6,7]
assert y == [[1,2,3,6,7], [4,5,6]]

import copy

assert = z == [[1,2,3,6,7], [4,5,6]]
z = copy.deepcopy(x)
assert not z is x

z[0].append(8)




