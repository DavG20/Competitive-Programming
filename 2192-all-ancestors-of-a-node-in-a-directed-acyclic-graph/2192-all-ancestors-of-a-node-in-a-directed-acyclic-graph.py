class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ans = [set() for _ in range(n)]
        in_degree = [0] * n
        graph = defaultdict(set)
        for parent, kid in edges:
            ans[kid].add(parent)
            graph[parent].add(kid)
            in_degree[kid] += 1
            
        # Use Topological sort to get direct parent's all ancestors    
        queue = deque([u for u, degree in enumerate(in_degree) if degree == 0])
        while queue:
            parent = queue.popleft()
            for kid in graph[parent]:
                ans[kid].update(ans[parent])
                in_degree[kid] -= 1
                if in_degree[kid] == 0:
                    queue.append(kid)
                    
        return [sorted(s) for s in  ans] 
        
