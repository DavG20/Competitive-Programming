def countingSort(arr):
    # Write your code here
    
    count_arr = [0 for _ in range(100)]
    
    #increment the count
    for num in arr :
        count_arr[num]+=1
    
    return count_ar