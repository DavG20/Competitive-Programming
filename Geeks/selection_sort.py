class Solution: 
    def select(self, arr, i):
        # code here 
        target_indx=i
        for indx in range(i+1,len(arr)):
            if arr[target_indx]>arr[indx]:
                target_indx=indx
        arr[i],arr[target_indx]=arr[target_indx],arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            self.select(arr,i)
