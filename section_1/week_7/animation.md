

# Animating Mario

Add new images

```
# Load images
background_image = pygame.image.load("mario_background.jpg").convert()
mario_image = {}
mario_image[0] = pygame.image.load("mario-1.png").convert()
mario_image[1] = pygame.image.load("mario-2.png").convert()
koopa_image = pygame.image.load("koopa.png").convert()

mario_image[0].set_colorkey((255,255,255))
mario_image[1].set_colorkey((255,255,255))
koopa_image.set_colorkey((255,255,255))
```

Create constants for facing left and right

```
# Game constants
ground = 270

LEFT = 0
RIGHT = 1
```

Change variable initalization to include the image index and the direction Mario is facing

```
# Initialize Mario's position
y_position = ground
x_position = 500
x_speed = 0
jumping = False
y_speed = 0
mi_idx = 0
mario_facing = LEFT
```

Edit keydown to change the direction mario is facing

```
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
```

Rewrite Mario rendering code to take into account whether he is currently running and which direction he is facing

```
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
```





