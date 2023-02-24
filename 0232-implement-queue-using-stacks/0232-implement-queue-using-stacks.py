class MyQueue:

    def __init__(self):
        
        
        self.stack = []
        
        self.rev_stack = []

    def push(self, x: int) -> None:
        
        # get the stack1 element 
        
        while self.stack:
            
            self.rev_stack.append(self.stack.pop())
            
        self.rev_stack.append(x)
        
        while self.rev_stack:
            
            self.stack.append(self.rev_stack.pop())
            
        

    def pop(self) -> int:
        
        return self.stack.pop()
        

    def peek(self) -> int:
        
        return self.stack[-1]
        

    def empty(self) -> bool:
        
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()