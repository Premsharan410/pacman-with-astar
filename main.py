import pygame
from home_screen import HomeScreen
from game import Game

def main():
    pygame.init()
    
    # Initialize home screen
    home_screen = HomeScreen()
    
    # Show home screen and wall
    if home_screen.run():
    
        game = Game()
        
        # Main game loop
        running = True
        clock = pygame.time.Clock()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r and (game.game_over or game.win):
                        game.reset()
                    elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        game.pacman.change_direction({
                            pygame.K_UP: "up",
                            pygame.K_DOWN: "down",
                            pygame.K_LEFT: "left",
                            pygame.K_RIGHT: "right"
                        }[event.key])
            
            # Update game state
            game.update()
            
            # Draw everything
            game.draw()
            
            # Cap the frame rate
            clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()