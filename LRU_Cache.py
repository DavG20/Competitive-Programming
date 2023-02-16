class LRUCache(object):
    def __init__(self,capacity):
        self.capacity=capacity 
        self.cach=collections.OrderedDict()
    def get(self,key):
        if key in self.cach:
            v=self.cach.pop(key)
            self.cach[key]=v 
            return v 
        else:
            return -1
    def put(self,key,value):
        if key in self.cach:
            self.cach.pop(key)
        else:
            if self.capacity>0:
                self.capacity-=1
            else:
                self.cach.popitem(last=False)
        self.cach[key]=value