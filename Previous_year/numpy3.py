import  numpy as np

l = [1, 2, 3, 4, 5, 6]
m = np.mat(l)
arr = np.array(l)

# DEEP COPY vs COPY
a = arr         # SHALLOW COPY: dependent on arr
b = np.copy(arr)        # DEEP COPY: independent from arr
arr[0] = 67
print("arr: ", arr)
print("a: ", a)
print("b: ", b)
a[1] = 5555
print("arr: ", arr)
print("a: ", a)

