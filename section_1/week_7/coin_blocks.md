
# Coin Blocks

Load the block image

```
block_image = pygame.image.load("block.png").convert()
```

Load the coin image

```
coin_image = pygame.image.load("coin.png").convert()
```

Initialize the coin count


```
# Initialize game starting parameters
lives = 3
level = 1
coins = 0
```

Add block initializaton 

```
 # Initalize block
block = None
coin_x = None
coin_y = None
```

Handle the coin block

- Randomly generate block when there isn't one
- Detect block collision if there is one

```
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
```

Render the coin count

```
# Render coin count
screen.blit(coin_image, [50, 50])
font = pygame.font.Font(None, 24)
text = font.render(" x " + str(coins), 1, (255, 255, 0))
screen.blit(text, (70, 52))
```

Render blocks and a coin animation

```
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
```
