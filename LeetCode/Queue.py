class Queue(object):
    def __init__(self):
        self.Stack=[]
    def push(self,x):
        print(len(self.Stack),"this is len")
        self.Stack.insert(len(self.Stack),x)
    def Pop(self):
        pop_return=self.Stack[0]
        self.Stack.remove(self.Stack[0])
        return pop_return
    def display(self):
        for i in self.Stack:
            print(i)
        
q=Queue()
q.push(9)
q.push(0)
q.push(2)
print(q.Pop())
q.display()