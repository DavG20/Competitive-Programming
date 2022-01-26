from posixpath import split
import re


def countingSort(arr):
    data=[0 for i in range(100)]
    for i in range(len(arr)):
        data[arr[i]]+=1
    return data
print(countingSort([1,1,3,2,1]))