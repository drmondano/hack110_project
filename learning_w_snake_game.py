"""Snake game!"""

import pygame, sys, random
from pygame.math import Vector2

class Snake:
    """Creating the Snake."""
    def __init__(self):
        """Constructor"""
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('assets/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('assets/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('assets/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('assets/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('assets/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('assets/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('assets/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('assets/body_bl.png').convert_alpha()

    def draw_snake(self):
        """Draws the snake!"""
        self.update_head_assets()
        self.update_tail_assets()
        # 3. updating te snake head
        for index, block in enumerate(self.body):
            # 1. need a rect for positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # 2. figure out direction of head
            if index == 0:
                screen.blit(self.head, body_rect)
            elif index == (len(self.body) - 1):
            # this is a great way for referencing the last item in a list!
                screen.blit(self.tail, body_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                # if x coord of previous and next is same, then HORIZONTAL
                    screen.blit(self.body_vertical, body_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, body_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, body_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, body_rect) 
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, body_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, body_rect)
                    
        # commented out!
        """for block in self.body:
            # create a rectangle
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw rectangle
            pygame.draw.rect(screen, (183, 111, 122), body_rect)"""
    
    def move_snake(self):
        """Moves the snake."""
        if self.new_block:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_block(self):
        self.new_block = True

    def update_head_assets(self):
        relation_to_head = self.body[1] - self.body[0]
        if relation_to_head == Vector2(1, 0):
            self.head = self.head_left
        elif relation_to_head == Vector2(-1, 0):
            self.head = self.head_right
        elif relation_to_head == Vector2(0, 1):
            self.head = self.head_up
        elif relation_to_head == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_assets(self):
        relation_to_tail = self.body[-2] - self.body[-1]
        if relation_to_tail == Vector2(1, 0):
            self.tail = self.tail_left
        elif relation_to_tail == Vector2(-1, 0):
            self.tail = self.tail_right
        elif relation_to_tail == Vector2(0, 1):
            self.tail = self.tail_up
        elif relation_to_tail == Vector2(0, -1):
            self.tail = self.tail_down

class Fruit:
    """Creating the fruits."""

    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        # create an x and y position
        # draw a square

    def draw_fruit(self):
        # create an x and y position 
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
            # only moving by the cell size creates the illusion of a grid
        # draw a square (comment below) now changed to an image
        # pygame.draw.rect(screen, (126, 166, 114),fruit_rect)
        screen.blit(apple, fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class Main:
    """Class containing the main game logic."""
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition the fruit
            self.fruit.randomize()
            # add another block to the snake
            self.snake.add_block()
    
    def check_fail(self):
        # check if snake outside of screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over():
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row *cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row *cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
                

pygame.init()

# creates artificial cells
cell_size = 40
cell_number = 20

# creation of *grid* on screen
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# importing images
apple = pygame.image.load('assets/apple.png').convert_alpha()

# events (they are all in caps by convention)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# creation of blocks
main_game = Main()
# OLD fruit = Fruit()
# OLD snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
        # triggered by ANY key press on keyboard, now looking for specific keys
            # temporarily replacing self.direction on specific key presses
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                    

    # section showing the visuals
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)