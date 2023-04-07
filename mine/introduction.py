import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 40
velocity = 10

run = True 
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False 
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 500 - width - velocity:
        x += velocity
    if keys[pygame.K_DOWN] and y < 500 - height - velocity:
        y += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
   

    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()