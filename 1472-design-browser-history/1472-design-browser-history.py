class Node:
    
    def __init__(self,url):
        
        self.val = url
        self.next = None
        self.prev = None
        
        

class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.head = Node(homepage)

        
        
        

    def visit(self, url: str) -> None:
        
        newNode = Node(url)
        
        newNode.prev = self.head
        
        self.head.next = newNode
                
        self.head = self.head.next
        
        

    def back(self, steps: int) -> str:
        while (steps and self.head.prev):
            steps -= 1
            
            self.head = self.head.prev
        return self.head.val
        
        
        

    def forward(self, steps: int) -> str:
        while (steps and self.head.next):
            steps -= 1
            
            self.head = self.head.next
        return self.head.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)