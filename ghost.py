import pygame
import random
from astar import AStar

class Ghost:
    def __init__(self, x, y, color, mode="chase"):
        self.x = x
        self.y = y
        self.color = color
        self.mode = mode
        self.path = []
        self.speed = 0.1
        self.progress = 0
        self.astar = AStar()
    
    def move(self, pacman, walls):
        # Every few steps, recalculate path to Pac-Man
        if not self.path or random.random() < 0.02:
            start = (int(self.x), int(self.y))
            goal = (int(pacman.x), int(pacman.y))
            self.path = self.astar.find_path(start, goal, walls)

        if self.path:
            next_node = self.path[0]
            if abs(self.x - next_node[0]) < 0.1 and abs(self.y - next_node[1]) < 0.1:
                self.path.pop(0)
            else:
                dx = next_node[0] - self.x
                dy = next_node[1] - self.y
                dist = (dx**2 + dy**2) ** 0.5
                if dist > 0:
                    self.x += (dx / dist) * self.speed
                    self.y += (dy / dist) * self.speed

    def draw(self, screen, grid_size):
        pygame.draw.circle(screen, self.color,
                           (int(self.x * grid_size + grid_size // 2),
                            int(self.y * grid_size + grid_size // 2)),
                           grid_size // 2 - 2)
