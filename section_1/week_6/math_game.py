import pygame
import sys
import random

# Highest number to be used in multiplication problems
MAX_MULTIPLICATION = 20

problems = {}
problems_on_screen = 1
answer = ""
score = 0

pygame.font.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            input_key = event.key
            
            if input_key == pygame.K_RETURN:
                try:
                    if int(answer) in problems.keys():
                        score = score + 1
                        del problems[int(answer)]
                except:
                    pass
                
                answer = ""
            elif input_key == pygame.K_BACKSPACE:
                answer = answer[:-1]
            elif input_key < 128:
                answer = answer + chr(input_key)
    
    if len(problems) < problems_on_screen:
        
        # Multiplication Problem
        number_1 = random.randint(0, MAX_MULTIPLICATION)
        number_2 = random.randint(0, MAX_MULTIPLICATION)
        
        key = number_1 * number_2
        problems[key] = {
            'problem': str(number_1) + " * " + str(number_2),
            'x_pos': random.randint(0, 625),
            'y_pos': 0,
            'speed': 1
        }
    
    # Move problems
    for key in list(problems.keys()):
        problem = problems[key]
        problem['y_pos'] = problem['y_pos'] + problem['speed']
        
        if problem['y_pos'] > 400:
            score = score - 1
            del problems[key]
        else:
            problems[key] = problem
    
    screen.fill((0, 0, 0))
    
    for key, problem in iter(problems.items()):
        font = pygame.font.Font(None, 24)
        text = font.render(problem['problem'], 1, (255, 0, 0))
        screen.blit(text, (problem['x_pos'], problem['y_pos']))
        
    font = pygame.font.Font(None, 24)
    text = font.render("Answer: " + answer, 1, (255, 0, 0))
    screen.blit(text, (25, 450))
    
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score), 1, (255, 0, 0))
    screen.blit(text, (600, 450))    

    pygame.display.flip()
    clock.tick(20)
    