import pygame
import sys

pygame.init()

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



while True:

    # Initialize level of game

    
    # Initialize Mario's position
    y_position = ground
    x_position = 100
    x_speed = 0
    jumping = False
    y_speed = 0

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

        # Render background
        screen.fill((0, 0, 0))
        screen.blit(background_image, [0, 0])

        # Render lives remaining
        

        # Render Mario
        screen.blit(mario_image, [x_position, y_position])

        # Render Koopas

        pygame.display.flip()

        clock.tick(30)

pygame.quit()
sys.exit()