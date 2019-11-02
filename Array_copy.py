from numpy import *

arr = array([1,2,3,4,5])

arr = arr + 5

print(arr)

arr1 = array([1,2,3,4,5])

arr2 = array([1,2,3,4,5])

arr3 = arr1 + arr2

print(arr3)

print(sin(arr1))
print(cos(arr1))
print(tan(arr1))
print(log(arr1))
print(sqrt(arr1))

print(concatenate([arr1,arr2]))

arr_1 = array([1,2,6,8,2])

arr_2 = arr_1

print(arr_1)
print(arr_2)
print(id(arr_1))
print(id(arr_2))

#Shallow copy  - copied array is dependent of the change in value of the parent array.

arr_2 = arr_1.view()

arr_1[1] = 3

print(arr_1)
print(arr_2)
print(id(arr_1))
print(id(arr_2))

#Deep copy - copied array is independent of the change in value of the parent array.

arr_2 = arr_1.copy()

arr_1[1] = 3

print(arr_1)
print(arr_2)
print(id(arr_1))
print(id(arr_2))
