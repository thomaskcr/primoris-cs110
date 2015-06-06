import pygame
import sys
import time
import random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 337))
clock = pygame.time.Clock()

# Load images
background_image = pygame.image.load("mario_background.jpg").convert()
mario_image = {}
mario_image[0] = pygame.image.load("mario-1.png").convert()
mario_image[1] = pygame.image.load("mario-2.png").convert()
koopa_image = pygame.image.load("koopa.png").convert()
block_image = pygame.image.load("block.png").convert()
coin_image = pygame.image.load("coin.png").convert()

mario_image[0].set_colorkey((255,255,255))
mario_image[1].set_colorkey((255,255,255))
koopa_image.set_colorkey((255,255,255))

# Game constants
ground = 270

LEFT = 0
RIGHT = 1

# Initialize game starting parameters
lives = 3
level = 1
coins = 0

while lives > 0:

    # Initialize level of game
    next_level = time.time() + 30
    
    # Initialize Mario's position
    y_position = ground
    x_position = 500
    x_speed = 0
    jumping = False
    y_speed = 0
    mi_idx = 0
    mario_facing = LEFT
    
    # Initialize Koopas
    koopa_turns = {}
    koopa_x_pos = {}
    
    # Initalize block
    block = None
    coin_x = None
    coin_y = None
    
    for i_koopa in range(0, level):
        koopa_turns[i_koopa] = random.randint(0, 60) * 10
        koopa_x_pos[i_koopa] = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                    mario_facing = LEFT
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                    mario_facing = RIGHT
                elif event.key == pygame.K_UP:
                    if not jumping:
                        jumping = True
                        y_speed = 8
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = 0

        # Change Mario's position
        x_position = x_position + x_speed

        if jumping:
            y_position = y_position - y_speed
            y_speed = y_speed - 1

            if y_position > ground:
                y_position = ground
                y_speed = 0
                jumping = False
            
        # Change Koopa's position
        for i_koopa in range(0, level):
            if koopa_x_pos[i_koopa] < koopa_turns[i_koopa]:
                koopa_x_pos[i_koopa] = koopa_x_pos[i_koopa] + 5
            elif koopa_x_pos[i_koopa] > koopa_turns[i_koopa]:
                koopa_x_pos[i_koopa] = koopa_x_pos[i_koopa] - 5
            else:
                koopa_turns[i_koopa] = random.randint(0, 60) * 10
        
        
        mario_rect = pygame.Rect(x_position, y_position + 16, 12, 16)
        
        # Detect Koopa Collision
        died = False
        for i_koopa in range(0, level):
            koopa_rect = pygame.Rect(koopa_x_pos[i_koopa], ground + 16, 12, 16)
            if mario_rect.colliderect(koopa_rect):
                lives = lives - 1
                died = True
                break
        
        if died:
            break
        
        # Handle coin block
        if block is None:
            if random.randint(1, 50) == 1:
                block = random.randint(0, 540)
        else:
            # Detect whether block has been collided
            block_rect = pygame.Rect(block, ground - 25, 16, 16)
            if mario_rect.colliderect(block_rect):
                coin_x = block
                coin_y = ground - 25
                coins = coins + level
                block = None
        
        # Render background
        screen.fill((0, 0, 0))
        screen.blit(background_image, [0, 0])
        
        # Render time remaining
        percent_time = round(((next_level - time.time()) / 30.0) * 100)
        pygame.draw.rect(screen, (0, 0, 255), (450, 25, 100, 10), 2)
        pygame.draw.rect(screen, (255, 0, 0), (450, 25, percent_time, 10), 0)

        # Render lives remaining
        for i_life in range(0, lives):
            screen.blit(mario_image[0], [50 + (i_life * 25), 25])
            
        # Render coin count
        screen.blit(coin_image, [50, 50])
        font = pygame.font.Font(None, 24)
        text = font.render(" x " + str(coins), 1, (255, 255, 0))
        screen.blit(text, (70, 52))

        # Render Mario
        if x_speed == 0:
            mi_idx = 0
        else:
            if mi_idx == 0:
                mi_idx = 1
            else:
                mi_idx = 0
            
        disp_image = mario_image[mi_idx]
        if mario_facing == LEFT:
            disp_image = pygame.transform.flip(mario_image[mi_idx], 1, 0)
        
        screen.blit(disp_image, [x_position, y_position])
        
        # Render Koopas
        for i_koopa in range(0, level):
            screen.blit(koopa_image, [koopa_x_pos[i_koopa], ground])
            
        # Render block
        if block is not None:
            screen.blit(block_image, [block, ground - 25])
            
        # Render coin animation
        if coin_x is not None:
            for i in range(0, level):
                screen.blit(coin_image, [coin_x + (i * 10), coin_y])
            coin_y = coin_y - 1
            if coin_y < (ground - 25 - 20):
                coin_x = None
                coin_y = None
            

        pygame.display.flip()

        clock.tick(30)
        
        if time.time() > next_level:
            level = level + 1
            break

print ("Game Over - Coins: " + str(coins))

pygame.quit()
sys.exit()
