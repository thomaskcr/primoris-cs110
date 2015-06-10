import pygame
import sys
import math

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 400))

pygame.draw.line(screen, (0, 0, 255), (0, 200), (400, 200))
pygame.draw.line(screen, (0, 0, 255), (200, 0), (200, 400))

for x_map in range(0, 400):
    x = (x_map - 200) / 10
    
    try:
        y = math.sqrt(36 - x**2)
        
        y_map = (y * 10) + 200
        y_map_neg = (-y * 10) + 200
        
        pygame.draw.circle(screen, (255, 0, 0), (x_map, int(y_map)), 2, 1)
        pygame.draw.circle(screen, (255, 0, 0), (x_map, int(y_map_neg)), 2, 1)
    except:
        pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.flip()
