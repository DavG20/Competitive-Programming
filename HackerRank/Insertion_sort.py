def insertionSort1(n, arr):
    # Write your code here
    
    
    target = arr[n-1]
    
    index = n - 2
    
    while index >= 0 and  target < arr[index]:
        
        arr[index + 1] = arr[index ]
        
        index -= 1
        print( *arr)
    arr[index + 1] = target
    
    print(*arr)