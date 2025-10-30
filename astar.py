class AStar:
    @staticmethod
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def find_path(self, start, goal, walls):
        frontier = []
        frontier.append((0, start))
        
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while frontier:
            frontier.sort()
            current = frontier.pop(0)[1]
            
            if current == goal:
                break
                
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_node = (current[0] + dx, current[1] + dy)
                
                if not (0 <= next_node[0] < 30 and 0 <= next_node[1] < 30):
                    continue
                if next_node in walls:
                    continue
                    
                new_cost = cost_so_far[current] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal, next_node)
                    frontier.append((priority, next_node))
                    came_from[next_node] = current
        
        path = []
        current = goal
        while current != start:
            path.insert(0, current)
            current = came_from.get(current, start)
            if current is None:
                return []
        
        return path