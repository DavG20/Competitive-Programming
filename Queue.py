class MyQueue(object):
    
    def __init__(self):
        self.stack=[]
        

    def push(self, x):
        self.stack.insert(len(self.stack),x)
        

    def pop(self):
       
        pop_value=self.stack[0]
        self.stack.remove(self.stack[0])
        return pop_value
        

    def peek(self):
       
        return self.stack[0]
        

    def empty(self):
        return len(self.stack)==0
        


