class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return False
        
        queue = deque([0])
        
        room_label = [i for i in range(len(rooms))]
        
        room_label = set(room_label)
        
        
        visited = set([0])
        
        
        
        
        while queue :
            
            curr_lev = len(queue)
            
            
            for i in range(curr_lev):
                curr_val = queue.popleft()
                
                for neighbour in rooms[curr_val]:
                    
                    if not neighbour in visited:
                        
                        visited.add(neighbour)
                        
                        queue.append(neighbour)
                        
        
        
        
        visited = set(sorted(visited))
        
        room_label = set(sorted(room_label))
        
        
                
                
                
                
            
            
        
        
        return room_label == visited
        