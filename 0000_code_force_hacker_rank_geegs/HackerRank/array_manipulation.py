def arrayManipulation(n, queries):
    # Write your code here
    arr =[0 for _ in range(n)]
    for query in queries:
        arr[query[0]-1] += query[2]
        if query[1] < n:
            arr[query[1]] -= query[2]
    
    for i in range(1,n):
        arr[i] = arr[i] + arr[i - 1]
    return(max(arr))
    