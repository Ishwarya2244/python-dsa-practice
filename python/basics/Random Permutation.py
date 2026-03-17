#Random Permutation
from numpy import random
import numpy as np
arr=np.array([1,2,3])
random.shuffle(arr) #The shuffle() method makes changes to the original array.
print(arr)

random.permutation(arr) #The permutation() method returns a re-arranged array(and leaves the original arrau un-changed).
print(arr)


#Import NumPy and create an array arr = np.array([1, 2, 3, 4, 5]). Use NumPy to randomly permute the elements of arr.
import numpy as np
arr=np.array([1,2,3,4,5])
print(random.permutation(arr))

#integers from 0 to 9 and generate a random permutation
arr1=np.array([0,1,2,3,4,5,6,7,8,9])
print(random.permutation(arr1))


#arr = np.array([10, 20, 30, 40, 50]), shuffle the array in-place
arr2=np.array([100,20,30,40,50])
random.shuffle(arr2)
print(arr2)
















