class Solution:
     def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        queue = deque()
        order = []
        for course, pre in prerequisites:
            
            graph[pre].append(course)
            indegree[course] += 1
            
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                
                indegree[neighbor] -= 1
               
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(order) != numCourses:
            return []
        
        return order