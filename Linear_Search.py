pos = -1
def search(list,n):
    for i in list:
        globals()['pos'] += 1 
        if i == n:
            return True

    return False


list = [1,2,6,5,7,9]
n = 5

if search(list,n):
    print("Found at ",pos+1)
else:
    print("Not found")
