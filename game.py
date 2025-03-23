import pygame
import random

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon!")

FPS = 60
clock = pygame.time.Clock()
score = 0
lives = 5

sound_1 = pygame.mixer.Sound('music.wav')
miss_sound = pygame.mixer.Sound('sound.wav')
get_sound = pygame.mixer.Sound('sound_1.wav')
sound_1.play(-1)

score_font = pygame.font.SysFont('calibri', 30)
title_font = pygame.font.SysFont('calibri', 31)
lives_font = pygame.font.SysFont('calibri', 29)
reset_font = pygame.font.SysFont('calibri', 40)

reset_text = reset_font.render("Press any key to reset the game", True, (227, 245, 66), (0, 0, 0))
reset_text_rect = reset_text.get_rect()
reset_text_rect.center = (WINDOW_WIDTH // 2, 150)

score_text = score_font.render("Score: " + str(score), True, (255, 255, 255), (0, 0, 0))
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

title_text = title_font.render("The Dragon feeder", True, (30, 156, 114), (0, 0, 0))
title_text_rect = title_text.get_rect()
title_text_rect.center = (WINDOW_WIDTH // 2, 26)

lives_text = lives_font.render("lives: " + str(lives), True, (255, 255, 255), (0, 0, 0))
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH - 40, 13)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.center = (30, 150)
dragon_speed = 6

coin_image = pygame.image.load("coin.png")   
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH + 20, 200)
coin_speed = 13

game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()

    coin_rect.x -= coin_speed
    if coin_rect.right < 0:                                    
        coin_rect.center = (WINDOW_WIDTH + 20, random.randint(40, WINDOW_HEIGHT - 40))
        lives -= 1
        lives_text = lives_font.render("lives: " + str(lives), True, (255, 255, 255), (0, 0, 0))
        miss_sound.play(0)
        if lives == 0:
            sound_1.stop()
            pause = True
            while pause:
                display_surface.blit(reset_text, reset_text_rect)    
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        sound_1.play(-1)
                        coin_speed = 6
                        score = 0
                        lives = 5
                        score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
                        lives_text = lives_font.render("Lives: " + str(lives), True, (255, 255, 255))
                        pause = False
                    if ev.type == pygame.QUIT:
                        game_running = False
                        pause = False
                pygame.display.update()

    if keys[pygame.K_UP] and dragon_right_rect.top > 48:
        dragon_right_rect.y -= dragon_speed
    if keys[pygame.K_DOWN] and dragon_right_rect.bottom < WINDOW_HEIGHT:
        dragon_right_rect.y += dragon_speed

    if dragon_right_rect.colliderect(coin_rect):
        coin_rect.center = (WINDOW_WIDTH + 20, random.randint(40, WINDOW_HEIGHT - 40))
        coin_speed += 0.5
        dragon_speed += 0.2
        if coin_speed >= 25:
            coin_speed = 25
        if dragon_speed >= 11:
            dragon_speed = 11

        score += 1
        score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
        get_sound.play(0)

    display_surface.fill((0, 0, 0))

    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    display_surface.blit(coin_image, coin_rect)
    pygame.draw.line(display_surface, (255, 255, 255), (0, 43), (WINDOW_WIDTH, 43), 5)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()