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
            heapq.heappush(heap, (-value,key))
        print(heap)
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return(result)

