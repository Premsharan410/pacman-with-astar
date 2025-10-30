import pygame
import sys
import os

class HomeScreen:
    def __init__(self, width=600, height=650):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pac-Man")
        self.width = width
        self.height = height
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.load_assets()
        
    def load_assets(self):
        # Try to load Pac-Man logo image
        try:
            self.logo = pygame.image.load(os.path.join('assets', 'pacman_logo.png'))
            self.logo = pygame.transform.scale(self.logo, (400, 200))
        except:
            # Fallback text if image not found
            self.logo = None
        
        # Colors
        self.yellow = (255, 255, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.button_color = (255, 255, 0)
        self.button_hover_color = (255, 255, 150)
        
        # Button
        self.button_rect = pygame.Rect(self.width//2 - 100, self.height//2 + 50, 200, 60)
        self.button_text = self.font_medium.render("START", True, self.black)
        
        # Ghost colors for decoration
        self.ghost_colors = [
            (255, 0, 0),    # Red
            (255, 182, 193), # Pink
            (0, 255, 255),  # Cyan
            (255, 165, 0)    # Orange
        ]
        
        # Animation variables
        self.animation_offset = 0
        self.animation_direction = 1
        
    def draw_button(self, mouse_pos):
        # Change color if hovering
        color = self.button_hover_color if self.button_rect.collidepoint(mouse_pos) else self.button_color
        
        pygame.draw.rect(self.screen, color, self.button_rect, border_radius=10)
        pygame.draw.rect(self.screen, self.black, self.button_rect, 2, border_radius=10)
        
        text_rect = self.button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(self.button_text, text_rect)
        
    def draw_ghosts(self):
        ghost_size = 40
        for i, color in enumerate(self.ghost_colors):
            x = 150 + i * 80 + self.animation_offset
            y = self.height - 100
            
            # Ghost body
            pygame.draw.rect(self.screen, color, 
                            (x, y, ghost_size, ghost_size), 
                            border_radius=ghost_size//4)
            
            # Ghost eyes
            eye_size = ghost_size // 5
            pygame.draw.circle(self.screen, self.white, 
                             (x + ghost_size//3, y + ghost_size//3), 
                             eye_size)
            pygame.draw.circle(self.screen, self.white, 
                             (x + 2*ghost_size//3, y + ghost_size//3), 
                             eye_size)
            
            # Pupils
            pupil_offset = eye_size // 2
            pygame.draw.circle(self.screen, self.black, 
                             (x + ghost_size//3 + pupil_offset, y + ghost_size//3), 
                             eye_size//2)
            pygame.draw.circle(self.screen, self.black, 
                             (x + 2*ghost_size//3 + pupil_offset, y + ghost_size//3), 
                             eye_size//2)
            
            # Feet
            for j in range(3):
                pygame.draw.circle(self.screen, color, 
                                 (x + j*ghost_size//3 + ghost_size//6, y + ghost_size), 
                                 ghost_size//6)
    
    def animate(self):
        self.animation_offset += self.animation_direction * 2
        if abs(self.animation_offset) > 20:
            self.animation_direction *= -1
    
    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if self.button_rect.collidepoint(mouse_pos):
                            return True  # Start game
            
            # Clear screen
            self.screen.fill(self.black)
            
            # Draw Pac-Man logo or text
            if self.logo:
                logo_rect = self.logo.get_rect(center=(self.width//2, 150))
                self.screen.blit(self.logo, logo_rect)
            else:
                title = self.font_large.render("PAC-MAN", True, self.yellow)
                title_rect = title.get_rect(center=(self.width//2, 150))
                self.screen.blit(title, title_rect)
            
            # Draw subtitle
            subtitle = self.font_small.render("Classic Arcade Game", True, self.white)
            subtitle_rect = subtitle.get_rect(center=(self.width//2, 220))
            self.screen.blit(subtitle, subtitle_rect)
            
            # Draw button
            self.draw_button(mouse_pos)
            
            # Draw decorative ghosts
            self.draw_ghosts()
            self.animate()
            
            # Draw instructions
            instructions = self.font_small.render("Use arrow keys to move", True, self.white)
            instructions_rect = instructions.get_rect(center=(self.width//2, self.height - 30))
            self.screen.blit(instructions, instructions_rect)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        return False

if __name__ == "__main__":
    home_screen = HomeScreen()
    if home_screen.run():
        print("Game starting...")
        # Here you would launch your main game