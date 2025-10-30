import pygame
import math

class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "right"
        self.next_direction = None
        self.speed = 0.1
        self.progress = 0
    
    def change_direction(self, new_dir):
        if new_dir in ["up", "down", "left", "right"]:
            self.next_direction = new_dir
    
    def move(self, walls):
        if self.progress == 0 and self.next_direction:
            new_x, new_y = self.x, self.y
            if self.next_direction == "right":
                new_x += 1
            elif self.next_direction == "left":
                new_x -= 1
            elif self.next_direction == "up":
                new_y -= 1
            elif self.next_direction == "down":
                new_y += 1
            
            if (new_x % 30, new_y % 30) not in walls:
                self.direction = self.next_direction
            self.next_direction = None
        
        if self.direction == "right":
            self.progress += self.speed
            if self.progress >= 1:
                self.x += 1
                self.progress = 0
        elif self.direction == "left":
            self.progress += self.speed
            if self.progress >= 1:
                self.x -= 1
                self.progress = 0
        elif self.direction == "up":
            self.progress += self.speed
            if self.progress >= 1:
                self.y -= 1
                self.progress = 0
        elif self.direction == "down":
            self.progress += self.speed
            if self.progress >= 1:
                self.y += 1
                self.progress = 0
        
        self.x %= 30
        self.y %= 30
    
    def draw(self, screen, grid_size):
        direction_factors = {
            "right": (1, 0),
            "left": (-1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }
        factor_x, factor_y = direction_factors.get(self.direction, (1, 0))
        
        screen_x = int(self.x * grid_size + self.progress * grid_size * factor_x)
        screen_y = int(self.y * grid_size + self.progress * grid_size * factor_y)
        
        pygame.draw.circle(screen, (255, 255, 0), 
                         (screen_x + grid_size // 2, screen_y + grid_size // 2), 
                         grid_size // 2 - 2)
        
        mouth_angle = {
            "right": (20, 340),
            "left": (160, 200),
            "up": (250, 290),
            "down": (70, 110)
        }.get(self.direction, (20, 340))
        
        pygame.draw.arc(screen, (0, 0, 0),
                       (screen_x + 2, screen_y + 2, grid_size - 4, grid_size - 4),
                       math.radians(mouth_angle[0]), math.radians(mouth_angle[1]), 2)