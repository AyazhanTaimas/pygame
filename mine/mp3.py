import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400,300))
done = False
x = 0 
i = 0
cnt = 0
songs = ['music//finnies.mp3', 'music//iwannabeyours.mp3', 'music//wakeupinthesky.mp3']

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.load(songs[x])
            pygame.mixer.music.play()
        
    pressed = pygame.key.get_pressed()
    
    #for i in range(len(songs)):
        #i = x
    if pressed[pygame.K_RIGHT]: 
        
        x = x + 1
        if x >= len(songs):
            x = 0
        pygame.mixer.music.load(songs[x])
        pygame.mixer.music.play()


        #i = i + 1
            
    if pressed[pygame.K_LEFT]:
         
        x = x - 1
        if x == 0:
            x = len(songs) - 1
        pygame.mixer.music.load(songs[x])
        pygame.mixer.music.play()

    if pressed[pygame.K_RETURN]:
        cnt = cnt + 1
        if cnt % 2 == 1:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

   
    pygame.display.flip()   
