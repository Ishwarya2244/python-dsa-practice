# NUMPY
# 07-12-2025

#*** Create a 1D NumPy array with 5 numbers and print ***

import numpy as np
array_1=np.array([1,2,3,4,5])
print(array_1)
print(array_1.ndim)
print(array_1.size)
print(array_1.shape)
print(array_1.dtype)


#***Create a 2D array with 2 rows and 3 columns***
array2=np.array([[1,2,3],[4,5,6]])
print(array2)
print(array2[0])
print(array2[1])

#*** Create 3 special arrays ***
array3=np.zeros((3,3))
print(array3)
array4=np.ones((2,2))
print(array4)
array5=np.full((3,1),7)
print(array5)

#***Create a range array using***
array6=np.arange(1,11)
print(array6)
array7=np.linspace(0,1,5)
print(array7)

#***Add, subtract, multiply two arrays***
a=np.array([10,20,30])
b=np.array([1,2,3])
print(a+b,a-b,a*b,a/b)

#***Create a 3×3 matrix and print***
array8=np.random.random((3,3))
print(array8)
print(array8.sum())
print(array8.max())
print(array8.min())
print(array8.sum(axis=0))
print(array8.sum(axis=1))

#***Reshape a 1D array of 12 numbers into 3×4 and 2×6***
array9=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape1=array9.reshape((3,4))
print(reshape1)
reshape2=array9.reshape((2,6))
print(reshape2)

#***Create a random array of shape (4,4) ***

array10=np.random.random((4,4))
print(array10)
print(array10.diagonal())
print(array10.sort())
print(np.sort(array10))
print(array10.mean())
print(array10.std())

#***Slice the array***
array11=np.array([10,20,30,40,50,60])
print(array11[1:4])
print(array11[3:])
print(array11[0::2])


