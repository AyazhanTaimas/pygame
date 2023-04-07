import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

done = False
x = 50
y = 50
r = 25
is_blue = True


clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if y > 0+45:
        if pressed[pygame.K_UP]: y -= 20
    if y < 500-45:
        if pressed[pygame.K_DOWN]: y += 20
    if x > 0+45:
        if pressed[pygame.K_LEFT]: x -= 20
    if x < 500-45:
        if pressed[pygame.K_RIGHT]: x += 20

    if is_blue: color = (100, 100, 250)
    else: color = (255, 100, 0)

    screen.fill((255,255,255))
    pygame.draw.circle(screen, color, (x, y), r)
    pygame.display.flip()
    clock.tick(60)

