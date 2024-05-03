import pygame
import random

pygame.init()#初始化pygame

WINDOW_WIDTH = 600#x
WINDOW_HEIGHT = 300#Y

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Feed the Dragon!")

FPS = 60
clock = pygame.time.Clock()


sound_1= pygame.mixer.Sound('music.wav')
sound_1.play(-1)

score_font = pygame.font.SysFont('calibri', 30) 
title_font = pygame.font.SysFont('calibri', 31)
lives_font = pygame.font.SysFont('calibri', 29)

score_text = score_font.render("Score: 0", True, (255, 255, 255), (0, 0, 0))
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10) 

title_text = title_font.render("The Dragon feeder", True, (30, 156, 114), (0, 0, 0))
title_text_rect = title_text.get_rect()
title_text_rect.center = (300,26)

lives_text = lives_font.render("lives: 5", True, (255, 255, 255), (0, 0, 0))
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (560,13) 





dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


game_running = True
while game_running:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            game_running = False
        
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_LEFT] and dragon_right_rect.left > 0:
        dragon_right_rect.x -= 5
    if keys[pygame.K_RIGHT] and dragon_right_rect.right < WINDOW_WIDTH:
        dragon_right_rect.x += 5
    if keys[pygame.K_UP] and dragon_right_rect.top > 0:
        dragon_right_rect.y -= 5
    if keys[pygame.K_DOWN] and dragon_right_rect.bottom < WINDOW_HEIGHT:
        dragon_right_rect.y += 5

    if dragon_right_rect.colliderect(coin_rect):
        coin_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT - 32)
    
        
    display_surface.fill((0,0,0))

    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    display_surface.blit(coin_image, coin_rect)
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()  
