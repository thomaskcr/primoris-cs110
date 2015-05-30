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
mario_image = pygame.image.load("mario.png").convert()
koopa_image = pygame.image.load("koopa.png").convert()
koopa_image.set_colorkey((255,255,255))

# Game constants
ground = 275

# Initialize game starting parameters
lives = 3
level = 1

while lives > 0:

    # Initialize level of game
    next_level = time.time() + 30
    
    # Initialize Mario's position
    y_position = ground
    x_position = 100
    x_speed = 0
    jumping = False
    y_speed = 0
    
    # Initialize Koopas
    koopa_turns = {}
    koopa_x_pos = {}
    
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
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
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
        died = False
        for i_koopa in range(0, level):
            koopa_rect = pygame.Rect(koopa_x_pos[i_koopa], ground + 16, 12, 16)
            if mario_rect.colliderect(koopa_rect):
                lives = lives - 1
                died = True
                break
        
        if died:
            break

        # Render background
        screen.fill((0, 0, 0))
        screen.blit(background_image, [0, 0])
        
        # Render time remaining
        percent_time = round(((next_level - time.time()) / 30.0) * 100)
        pygame.draw.rect(screen, (0, 0, 255), (450, 25, 100, 10), 2)
        pygame.draw.rect(screen, (255, 0, 0), (450, 25, percent_time, 10), 0)

        # Render lives remaining
        for i_life in range(0, lives):
            screen.blit(mario_image, [50 + (i_life * 25), 25])

        # Render Mario
        screen.blit(mario_image, [x_position, y_position])

        # Render Koopas
        for i_koopa in range(0, level):
            screen.blit(koopa_image, [koopa_x_pos[i_koopa], ground])

        pygame.display.flip()

        clock.tick(30)
        
        if time.time() > next_level:
            level = level + 1
            break

pygame.quit()
sys.exit()