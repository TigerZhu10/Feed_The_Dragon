import pygame

pygame.init()#初始化pygame

WINDOW_WIDTH = 600#x
WINDOW_HELGHT = 300#Y

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HELGHT))

pygame.display.set_caption("Feed the Dragon!")

sound_1= pygame.mixer.Sound('sound_1.wav')
sound_2= pygame.mixer.Sound('sound_2.wav')

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

sound_2.set_volume(.1)
sound_2.play()

pygame.mixer.music.load('music.wav')

pygame.mixer.music.play(-1,2.1)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

GREEN = (0,255,0)
DARKGREEN = (10,50,10)
BLACK = (0,0,0)



game_running = True
while game_running:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            game_running = False



    pygame.display.update()

pygame.quit()  

