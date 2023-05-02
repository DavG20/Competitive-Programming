class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """


        dir_ver = [(1 , 0) , (-1 , 0) , (0, 1 ) , (0 , -1)]

        inbound = lambda x , y : 0 <= x <  len(maze) and 0 <= y < len(maze[0])

        xr , yc = (entrance[0] , entrance[1])
        
        queue = deque([(xr , yc)])

        visited = set(((xr , yc)))

        count = 0
        while queue: 

            curr_lev = len(queue)
            for i in range(curr_lev):

                curr_x , curr_y = queue.popleft()
                if ((curr_x == 0 or curr_x == len(maze) - 1) or (curr_y == 0 or curr_y == len(maze[0] ) - 1 )) and not (curr_x == xr and curr_y == yc ):
                    
                    return count 

                for dx , dy in dir_ver:

                    if inbound(curr_x + dx , curr_y + dy) and maze[curr_x + dx][curr_y + dy] == ".":
                        
                        if (curr_x + dx , curr_y + dy) not in visited:

                            visited.add((curr_x + dx , curr_y + dy))
                            queue.append((curr_x + dx , curr_y + dy))
            count += 1
        return -1


