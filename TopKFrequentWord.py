import heapq

class Solution:
    def topKFrequent(self,words,k):
        result=[]
        count={}
        for word in words:
            count[word]=count.get(word,0)+1
        print(count)
        heap=[]
        for key,value in count.items():
            print(value,key)
            heapq.heappush(heap, (-value,key)) #this will insert the values to the heap root becase the largest value become smallest 
        print(heap)
        for i in range(k):
            result.append(heapq.heappop(heap)[1]) #this heappop will return the smalest value in the heap means the most frequent val
        return(result)

