class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        uf = UnionFind(len(s))
        
        for a, b in pairs:
            uf.union(a, b)

		
        group = defaultdict(lambda: ([], []))  
        
        for i, ch in enumerate(s):
            parent = uf.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

	
        print(group.values())
        
        res = [''] * len(s)
		# print(res)
        #sorting 
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)
        
        
        

    
class UnionFind:
    
    def __init__(self , n):
        
        self.Parent = [i for i in range(n)]
        
    def union(self, a, b):
        self.Parent[self.find(a)] = self.find(b)
		
    def find(self, a):
        if self.Parent[a] != a:
            self.Parent[a] = self.find(self.Parent[a])

        return self.Parent[a]