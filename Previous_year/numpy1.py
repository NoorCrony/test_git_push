import numpy as np

a = np.array([1,2,3,4])
print(a)
print(type(a))
# warning different data type string
a = np.array([1,2,3,"Noor", 2.2])
print(a)
# data type hierarchy
a = np.array([1,2,3, 2.2])
print(a)
# warning different dtype
a = np.array([1, 2, 3, 2.2, (2+7j)])
print(a)
a = np.array([[1, 2, 3, 2.2], [(2+7j)]])
print(a)
a = np.array([[1, 2], [2,3]])
print(a)
a = np.array([[[1,2,3],[2,1,2],[2,3,1]]])
print(a)
# dimension input
a = np.array([1,2], ndmin = 3)
print(a)
# type conversion
a = np.array([1,2], dtype = complex)
print(a)
# tuple is also accepted
a = np.array([(1,2), (2,3)])
print(a)
# type customised
a = np.array([(1,2), (2,3)], dtype= [("a", '<i2'), ("b", '<i8')])
print(a)
print(type(a[0][0]))
print(type(a[0][1]))
print(type(a[1][0]))
print(type(a[1][1]))

a = np.mat(a)
print(type(a))



