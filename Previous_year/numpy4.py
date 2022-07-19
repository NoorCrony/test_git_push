import numpy as np

l = [1, 2, 3, 4, 5, 6]
m = np.mat(l)
arr = np.array(l)
print(arr[0:3])

for k in arr:
    print(k)
print(type(np.fromfunction(lambda i, j: i == j, (4, 4))))
print(np.fromfunction(lambda i, j: i == j, (4,4)))
print(np.fromfunction(lambda i, j: i**j, (3,3)))
print(np.fromfunction(lambda i, j: i/j, (3,3)))

print("FROMITER")
g = [(i*i for i in range(5))]
a = np.fromiter(range(5), dtype="int")
print(a)
print(type(a))

print("FROMSTRING")
a = np.fromstring('1 2 3 4', sep=" ", dtype=complex)
print(a)
print(type(a))

a = np.fromfunction(lambda i, j: i/j, (3, 3))

print("arr.ndim")
print(a.ndim)

print("arr.size")
print(a.size)

print("arr.shape")
print(a.shape)

print("arr.dtype")
print(a.dtype)

a = np.array([[[1,2,3,4],[1,22,3,4]],[[1,2,5,66],[5,7,8,90]]])
print("arr.shape")
print(a.shape)


