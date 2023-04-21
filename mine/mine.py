import pygame, sys 

widht = 500
height = 500

screen = pygame.display.set_mode((widht, height))

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
screen.fill(black)

speed = 10
FPS = 60
FramePerSecond = pygame.Clock.time()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        speed += 5    