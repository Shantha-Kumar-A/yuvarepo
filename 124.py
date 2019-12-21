def findlowocc(listval):
    tempval = 0
    for i in range(len(listval)-1,0,-1):
        for j in range(i):
            if listval[j] > listval[j+1]:
                temp = listval[j]
                listval[j] = listval[j+1]
                listval[j+1] = temp

    for k in listval:
        if k == tempval:
            return k
        tempval = k

list = [112,55,15,66,55,120,116]
print(findlowocc(list))

