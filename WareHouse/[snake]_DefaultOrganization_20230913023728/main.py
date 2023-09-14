'''
This is the main file of the Snake Game application.
'''
import pygame
import sys
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
# Define game variables
snake_size = 20
snake_speed = 15
clock = pygame.time.Clock()
# Snake class
class Snake:
    def __init__(self):
        '''
        Initialize the Snake object.
        '''
        self.length = 1
        self.positions = [(window_width // 2, window_height // 2)]
        self.direction = (1, 0)  # Initial direction is right
    def get_head_position(self):
        '''
        Get the position of the snake's head.
        '''
        return self.positions[0]
    def move(self):
        '''
        Move the snake in the current direction.
        '''
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * snake_size)) % window_width, (cur[1] + (y * snake_size)) % window_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    def reset(self):
        '''
        Reset the snake to its initial state.
        '''
        self.length = 1
        self.positions = [(window_width // 2, window_height // 2)]
        self.direction = (1, 0)  # Reset direction to right
    def draw(self, surface):
        '''
        Draw the snake on the given surface.
        '''
        for p in self.positions:
            pygame.draw.rect(surface, green, (p[0], p[1], snake_size, snake_size))
# Game class
class Game:
    def __init__(self):
        '''
        Initialize the Game object.
        '''
        self.snake = Snake()
    def run(self):
        '''
        Run the game loop.
        '''
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):  # Prevent going back
                        self.snake.direction = (1, 0)
                    elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.direction = (-1, 0)
                    elif event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.direction = (0, 1)
            self.snake.move()
            if self.snake.get_head_position() in self.snake.positions[1:]:
                self.snake.reset()
            window.fill(black)
            self.snake.draw(window)
            pygame.display.update()
            clock.tick(snake_speed)
        pygame.quit()
        sys.exit()
# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()