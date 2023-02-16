def insertionSort1(n, arr):
    temp_index=0
    temp=arr[n-1]
    for i in range(n):
        # print(n-i)
        if(temp<arr[n-1-i]):
            arr[n-1-i],arr[n-i]=arr[n-1-i],arr[n-i-1]
            temp_index=n-i-1
        else:
            temp_index=n-i
            print(temp_index)
    arr[temp_index]=temp
    return arr