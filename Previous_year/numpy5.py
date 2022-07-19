import numpy as np

l = [1, 2, 3, 4, 5, 6]
m = np.mat(l)
arr = np.array(l)

# l = list(range(6.6))    # can not give floating point INPUT
l = np.arange(6.6, 7.3, 0.3)      # Can give floating point INPUT
print("Includes upper bound for FLOAT \n", l)
print
# Upper Bound is included unlike range()
l = np.arange(8, 10)      # Can give floating point INPUT
print("Excludes upper bound for INT \n", l)

line_space = np.linspace(1, 3, 17)
print(line_space)
line_space = np.linspace([1, 10], 3, 17, axis=1)
print(line_space)
line_space = np.linspace([1, 10], [3, 12], 17, axis=1)
print(line_space)

z = np.zeros((1, 2, 3))
o = np.ones((1, 4))
e = np.empty((2, 4))
I = np.eye(3)
print(type(z), type(o), type(e))
print(I)

log = np.logspace(1, 4, 3)
print(log)
