from numpy import *

arr1 = array([
               [1,2,3],
               [4,5,6]
                ])

print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()

print(arr2)

arr3 = arr2.reshape(2,3)

print(arr3)

arr4 = arr2.reshape(1,2,3)

print(arr4)

#Matrix

m = matrix(arr1) #using an array

print(m)

m = matrix('1 2 3; 4 5 6; 7 8 9') #using the values from the user

print(m)

print(diagonal(m)) #printing the diagonal elements alone


m1 = matrix('1 2 3; 4 5 6; 7 8 9')

m2 = matrix('1 2 3; 4 5 6; 7 8 9')

m3 = m1 + m2

print(m3)

m4 = m1 * m2

print(m4)

print(m1[0,2])

#print(m1[0].reshape(3,1))

v1_1 = 0
for h in range(0,3):
    for i in range(0,3):
        for j in range(0,3):
            v1 = m1[i,j] * m2[j,i]
            v1_1 = v1 + v1_1
        ar1 = []
        ar1.append(v1_1)
        print(ar1)
    ar2 = []
    ar2.append(ar1)
m5 = matrix(ar2)
print(m5)
    

    
