def calcavgdist(cord1,cord2,cord3):
    temp1 = cord1[0] + cord2[0] + cord3[0]
    temp2 = cord1[1] + cord2[1] + cord3[1]
    avgdist = (temp1 + temp2) / 3
    return avgdist

if __name__ == '__main__':
    cord1 = [1,2]
    cord2 = [2,3]
    cord3 = [4,6]
    print(calcavgdist(cord1,cord2,cord3))    

def reverse(s):
    return s[:: -1]
def isPalindrome(str):
    rev = reverse(str)
    if rev == str:
        return True
    return False

print(isPalindrome("abcddcba"))
  
