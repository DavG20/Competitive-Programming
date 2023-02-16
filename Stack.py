class MinStack(object):
    
    def __init__(self):
        self.Stack=[]
        

    def push(self, val):
        self.Stack.insert(0,val)
        

    def pop(self):
        self.Stack.remove(self.Stack[0])
        

    def top(self):
        return self.Stack[0]
        

    def getMin(self):
        return min(self.Stack)
        
