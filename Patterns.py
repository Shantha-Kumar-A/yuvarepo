for i in range(4):
        for j in range(4):
            print("# ",end="")
        print("")
    
for i in range(4):
    for j in range(i+1):
        print("#",end="")
    print("")
for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print("")
for i in range(4):
    for j in range(4-i):
        print(j+i+1,end="")
    print("")
str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ : i+1 ] + str2[ i : ])    
