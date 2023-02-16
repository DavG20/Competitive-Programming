def countSwaps(a):
    # Write your code here
    count=0
    for i in range(len(a)):
        
        for j in range(i+1,len(a)):
            
            if a[i]>a[j]:
                count+=1
                a[i] , a[j] = a[j] , a[i]
    print("Array is sorted in",count,"swaps.")
    print ("First Element:",a[0])
    print("Last Element:" ,a[-1])
