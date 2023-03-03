class MyCircularDeque:

    def __init__(self, k: int):
        
        self.cap = k
        
        self.size = 0
        
        self.front = 0
        
        
        self.queue = [0 for _ in range(k)]
        
        

    def insertFront(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        
        # lets add from the end 
        # this will gave us the index to be add from the end
        
        self.front = (self.front - 1 + self.cap) % self.cap  
        
        self.queue[self.front] = value
        
        self.size += 1
        
        return True
        

    def insertLast(self, value: int) -> bool:
        
        if self.isFull() :
            
            return False
        #this code will gave us the index from the start onward
        
        rear = (self.front + self.size ) % self.cap
        
        self.queue[rear] = value
        
        self.size += 1
        
        return True
        
        
        
        
        

    def deleteFront(self) -> bool:
        
        # front = (front - 1 + self.cap) % self.cap
        
        if self.isEmpty():
            
            return False 
        
        self.front = (self.front + 1 ) % self.cap
        
        self.size -= 1
        
        # front = (front + 1 + self.cap) % self.cap
        
        return True
        
        

    def deleteLast(self) -> bool:
        
        if self.isEmpty() :
            return False
        
        
        
        
        
        self.size -= 1
        
        return True
        

    def getFront(self) -> int:
        
        if self.isEmpty():
            
            return -1
        
        return self.queue[self.front]
        
        
        

    def getRear(self) -> int:
        
        rear = (self.front  - 1 + self.size ) % self.cap
        
        if self.isEmpty():
            
            return -1
        
        # rear = (front - 1 + self.size ) % self.cap
        
        return self.queue[rear]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        
        return self.size == self.cap
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()