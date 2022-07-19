import numpy as np
# INDEX Mult
# Matrix Mult
# BROADCASTING
a = [[1, 1, 2],
     [2, 3, 1],
     [1, 0, 0]]

b = [[0, 3, 2],
     [3, 3, 1],
     [1, 0, 0]]
a = np.array(a)
b = np.array(b)

index_mult = a*b
matrix_mult = a @ b
print(index_mult)
print(matrix_mult)

# BROADCASTING
d = np.zeros((4,4), dtype= int)
e = np.array([1, 2, 3, 4])
print(d+5)     # BOTH ROW & COLUMN
print(d+e)     # ROW WISE BROADCASTING
print(d + e.reshape(4, 1))     # COLUMN WISE BROADCASTING

rrr = np.ones([1,4])
print(rrr)
rrr = rrr.T
print(rrr)

# SQRT, EXP, LOG10, SQUARE
d = np.random.rand(2,3)
print(d)
print(np.sqrt(d))
print(np.exp(d))
