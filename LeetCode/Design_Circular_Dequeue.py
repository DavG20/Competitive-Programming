from turtle import clear


class MyCircularDeque(object):
    
    def __init__(self, k):
        """
        :type k: int
        """
        self.Stack=[]
        self.size=k
       
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        temp=len(self.Stack)<self.size
        if(temp):
            self.Stack.insert(0,value)
        return temp
       
        
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        temp=len(self.Stack)<self.size
        if temp:
            self.Stack.insert(len(self.Stack),value)
        return temp
    def display(self):
        for i in self.Stack:
            print(i)
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        temp=len(self.Stack)>=1
        if temp:
            self.Stack.remove(self.Stack[0])
        
        return temp

    def deleteLast(self):
        """
        :rtype: bool
        """
        temp=len(self.Stack)>=1
        if temp:
            self.Stack.remove(self.Stack[len(self.Stack)-1])
        return temp
        
        

    def getFront(self):
        """
        :rtype: int
        """
        if(len(self.Stack)==0):
            return -1
        else:
            return self.Stack[0]
        
        

    def getRear(self):
        """
        :rtype: int
        """
        if(len(self.Stack)==0):
            return -1
        else:
            return self.Stack[len(self.Stack)-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.Stack==[]
    
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.Stack)==self.size
        