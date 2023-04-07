import pygame , sys , random , time , os
from pygame.locals import *
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
Green = (0, 255, 0)
size = [400, 600]
cnt = 0
e_library_of_images = {}

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Racer game")

icon = pygame.image.load("images/vehicle.png") #
pygame.display.set_icon(icon)

background = pygame.image.load("images/road.png")

FPS = 60
FramePerSec = pygame.time.Clock()

running = True

coinFont = pygame.font.SysFont("childer", 40)
font_style=pygame.font.SysFont("bahnschrift", 20)
# screen.fill(WHITE)


class Player(pygame.sprite.Sprite): 
    def init(self):
        super().init() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 550) 
        self.speed = 5 
    def move(self): 
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 400:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(self.speed, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 600:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.speed)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def init(self): 
        super().init()
        self.rand = random.randint(1, 6)
        print(self.rand)
        # self.image = get_images(f'{str(self.rand)}.png')
        # self.image = get_images(f'{self.rand}.png')
        self.image = pygame.image.load(f'images/Enemy'+f'/{self.rand}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, 400 - 40), 0)
        self.speed2 = 10
    
    def move(self):
        self.rect.move_ip(0, self.speed2) 
        self.speed2 +=0.001
        if (self.rect.bottom > 610): 
            self.rect.top = 0                
            self.E = random.randint(1, 6)
            print(self.E)
            # self.image = get_images(f'{str(self.E)}.png')
            self.image = pygame.image.load(f'images/Enemy' + f'/{self.E}.png' )
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(20, 360), 0)   


    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coins(pygame.sprite.Sprite): 
    def init(self):
        super().init()
        self.y = random.randint(1, 1)
        self.image = pygame.image.load(f'images/Coin'+f'/{self.y}.png') 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(10, 390), 25) 
        self.speed3 = 5
    
    def move(self):
        self.speed3 += 0.001
        self.rect.move_ip(0, self.speed3) 
        if self.rect.bottom > 600: 
            self.rect.top = 0 
            self.rect.center = (random.randint(20, 360), 10)
            self.x = random.randint(1, 1)
            self.image = pygame.image.load(f'images/Coin'+f'/{self.x}.png')
            # if self.x == 2:
            #     cnt+=100
class Bonuscoin(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load(f'images/Coin/2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, 390), 100)
        self.speed = 5
    
    def move(self):
        self.speed4 = 10
        if cnt % 10 == 0 and cnt != 0:
            self.rect.move_ip(0, self.speed4)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(20, 360), 10)
            self.image = pygame.image.load(f'images/Coin/2.png')
            
            
P1 = Player()
E1 = Enemy()
C1 = Coins()
B1 = Bonuscoin()
enemies = pygame.sprite.Group() 
enemies.add(E1)
bonus = pygame.sprite.Group()
bonus.add(B1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
new_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
new_sprites.add(B1)

# def mus():
#     pygame.mixer.music.load('game.mp3')
#     pygame.mixer.music.play()
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
    score = coinFont.render(str(cnt), True, RED)
    scoreen = coinFont.render('Your score:', True, Green)

    screen.blit(background, (0, 0))
    screen.blit(score, (350, 25))
    screen.blit(scoreen, (195, 22.5))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    if cnt%10 == 0 and cnt == 0:
        for x in new_sprites:
            screen.blit(x.image, x.rect)
            x.move()
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.mp3').play()
        photo = pygame.image.load("images/gameover.jpg")   
        screen.blit(photo, (30, 60))
        print("You lose dumb!")
        print(f"Your score is:{cnt}")
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    if pygame.sprite.spritecollideany(P1, coins ):
        pygame.mixer.Sound('coin.mp3').play()
        cnt+=1
        C1.rect.top = 600
    if pygame.sprite.spritecollideany(P1,bonus):
        pygame.mixer.Sound('coin.mp3').play()
        cnt+=2
        B1.rect.top = 600
    pygame.display.update()
    pygame.display.flip()
    FramePerSec.tick(FPS)