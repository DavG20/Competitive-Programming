
import sys
def countSwaps(a):
    # Write your code here
    countSwap=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(a[j]>a[j+1]):
               a[j],a[j+1]=a[j+1],a[j]
               countSwap+=1
    sys.stdout.write("Array is sorted in "+str(countSwap)+" swaps. \n")
    sys.stdout.write("First Element: "+ str(a[0])+"\n")
    sys.stdout.write("Last Element: "+str(a[len(a)-1])+"\n")

