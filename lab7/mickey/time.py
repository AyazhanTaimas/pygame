import pygame
import sys
import datetime


COLOR_BACK = (250, 255, 255)
size = [830, 780]

screen = pygame.display.set_mode(size)
mickey = pygame.image.load("images/mickey.png")
left_hand = pygame.image.load('images/left-hand.png')
right_hand = pygame.image.load('images/right-hand.png')
# icon = pygame.image.load('images/mickeyicon3.png')
# pygame.display.set_icon(icon)
pygame.display.set_caption("Mickey Clock")

def blitRotateCenter(surface, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surface.blit(rotated_image, new_rect)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exist")
            pygame.quit()
            sys.exit()
    screen.fill(COLOR_BACK)
    screen.blit(mickey,(0, 0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second   

    blitRotateCenter(screen, left_hand, (340, 150), second* -6)
    blitRotateCenter(screen, right_hand, (320, 215), minute* -6)
    pygame.display.flip()
    clock.tick(60)