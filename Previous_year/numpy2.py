import  numpy as np

l = [1, 2, 3, 4, 5, 6]
m = np.mat(l)
# methods to convert to array
# outputs are same
a = np.array(l)
b1 = np.asarray(l)
b2 = np.asarray(m)
c1 = np.asanyarray(l)
c2 = np.asanyarray(m)   # m is already an array
print("a: ", a)
print(b1)
print(b2)   # matrix to array
print(c1)
print(m)
print(c2)   # remains a matrix - NO CONVERSION

print(issubclass(np.matrix, np.ndarray))
print(issubclass(np.ndarray, np.matrix))
