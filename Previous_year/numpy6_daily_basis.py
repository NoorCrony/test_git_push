import numpy as np

d = np.linspace(4, 7, 40)
print(d.ndim)
print(d.shape)

# TRANSPOSE: row to column
d = d.reshape(40,1)
print(d)
d = d.reshape(2, 2, 10)
print(d)
# RANDOM Values
d = np.random.rand(3)
print(d)
d = np.random.randn(3,3,2)
print(d)
d = np.random.randint(2,6,(4,2))
print(d)
d = d.reshape(2,-1) # Automatically gets reshape value
print(d)
print(d.max())


