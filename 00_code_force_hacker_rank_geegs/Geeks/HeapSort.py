class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        largest=i
        l=2*i +1
        r=2*i +2
        if l<n and arr[i]<arr[l]:
            largest=l
        if r<n and arr[r]>arr[largest]:
            largest=r
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        pass
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        for i in range(n//2, -1, -1):
          self.heapify(arr, n, i)
          
        for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]
  
          # Heapify root element
          self.heapify(arr, i, 0)
