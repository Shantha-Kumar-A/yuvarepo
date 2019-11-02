pos = -1
def search(list,n):
    l = 0
    u = len(list) - 1
    for i in list:
        mid = (l+u) // 2 #integer division to get the int value after division
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list = [1,2,55,6,99,148,154545,25,65465]
n = 1455

if search(list,n):
    print("Found at ",pos+1)
else:
    print("Not found")
