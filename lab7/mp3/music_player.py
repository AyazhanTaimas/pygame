import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400,300))
done = False 
i = 0
cnt = 0
songs = ['music//finnies.mp3', 'music//iwannabeyours.mp3', 'music//wakeupinthesky.mp3']
pygame.mixer.music.load(songs[i])

def music_play():
    pygame.mixer.music.play()
def next_song():
    global i
    i += 1
    if i >= len(songs):
        i = 0
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play()   
    
def prev():
    global i
    i -= 1
    if i == 0:
        i = len(songs) - 1
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play()
    
def start():
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.pause()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                music_play()
            if event.key == pygame.K_LEFT : 
                prev()
            if event.key == pygame.K_RIGHT : 
                next_song()
            if event.key == pygame.K_RETURN : 
                stop()
            if event.key == pygame.K_SPACE : 
                start()
            
            
    
            
    
    #if pressed[K_SPACE]: start()
    #pygame.display.update()
    pygame.display.flip()


    
