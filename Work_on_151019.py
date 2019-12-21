# for i in range(-6,0):
# 	print(i)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    tempval = 0.0
    sum_list = []
    for i in range(0,len(arr)):
        s_arr = []
        s_arr = sorted(arr)
        s_arr.remove(arr[i])
        # print(s_arr)
        tempval = 0
        for j in range(0,len(s_arr)):
            tempval = tempval + s_arr[j]
        #print(tempval)
        sum_list.append(tempval)
    sum_list.sort()
    # print(sum_list)
    print(sum_list[0],sum_list[len(sum_list)-1])



if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [140638725, 436257910, 953274816, 734065819, 362748590]

    miniMaxSum(arr)
