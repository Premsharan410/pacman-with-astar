class Maze:
    def __init__(self):
        self.walls = self.create_maze()
        self.dots = self.create_dots()
    
    def create_maze(self):
        walls = set()
        
        # Outer walls
        for x in range(30):
            walls.add((x, 0))
            walls.add((x, 29))
        for y in range(30):
            walls.add((0, y))
            walls.add((29, y))
        
        # Inner walls
        for x in range(5, 25):
            walls.add((x, 5))
            walls.add((x, 24))
        
        for y in range(5, 25):
            walls.add((5, y))
            walls.add((24, y))
            
        # Central block with opening
        for x in range(10, 20):
            for y in range(10, 20):
                if not (14 <= x <= 16 and 14 <= y <= 16):  # Leave center open
                    walls.add((x, y))
        
        return walls
    
    def create_dots(self):
        dots = []
        for x in range(1, 29):
            for y in range(1, 29):
                if (x, y) not in self.walls and not (x == 15 and y == 15):
                    dots.append((x, y))
        return dots