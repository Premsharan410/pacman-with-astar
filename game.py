import pygame
from pacman import PacMan
from ghost import Ghost
from maze import Maze

class Game:
    def __init__(self):
        self.width = 600
        self.height = 650
        self.grid_size = 20
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pac-Man with AI Ghosts")
        self.font = pygame.font.SysFont('Arial', 24)
        self.reset()
        
    def reset(self):
        self.score = 0
        self.maze = Maze()
        self.pacman = PacMan(15, 15)
        self.ghosts = [
            Ghost(5, 5, (255, 0, 0), "chase"),
            Ghost(25, 5, (255, 182, 193), "ambush"),
            Ghost(5, 25, (0, 255, 255), "random"),
            Ghost(25, 25, (255, 165, 0), "patrol")
        ]
        self.game_over = False
        self.win = False
    
    def update(self):
        if self.game_over or self.win:
            return
            
        self.pacman.move(self.maze.walls)
        
        for ghost in self.ghosts:
            ghost.move(self.pacman, self.maze.walls)
        
        pacman_pos = (int(self.pacman.x), int(self.pacman.y))
        for ghost in self.ghosts:
            ghost_pos = (int(ghost.x), int(ghost.y))
            if pacman_pos == ghost_pos:
                self.game_over = True
                break
                
        for dot in self.maze.dots[:]:
            if pacman_pos == dot:
                self.maze.dots.remove(dot)
                self.score += 10
                if not self.maze.dots:
                    self.win = True
                break
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        # Draw walls
        for wall in self.maze.walls:
            pygame.draw.rect(self.screen, (0, 0, 139), 
                           (wall[0] * self.grid_size, wall[1] * self.grid_size, 
                            self.grid_size, self.grid_size))
        
        # Draw dots
        for dot in self.maze.dots:
            pygame.draw.circle(self.screen, (255, 255, 255), 
                             (dot[0] * self.grid_size + self.grid_size // 2, 
                              dot[1] * self.grid_size + self.grid_size // 2), 
                             2)
        
        # Draw characters
        self.pacman.draw(self.screen, self.grid_size)
        for ghost in self.ghosts:
            ghost.draw(self.screen, self.grid_size)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, self.height - 40))
        
        if self.game_over:
            game_over_text = self.font.render("GAME OVER! Press R to restart", True, (255, 0, 0))
            self.screen.blit(game_over_text, (self.width // 2 - 150, self.height // 2))
        elif self.win:
            win_text = self.font.render("YOU WIN! Press R to restart", True, (255, 255, 0))
            self.screen.blit(win_text, (self.width // 2 - 120, self.height // 2))
        
        pygame.display.flip()