import pygame

pygame.init()#初始化pygame

WINDOW_WIDTH = 600#x
WINDOW_HELGHT = 300#Y

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HELGHT))

pygame.display.set_caption("Feed the Dragon!")

dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (600,0)

game_running = True
while game_running:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            game_running = False

    display_surface.blit(dragon_right_image, dragon_right_rect)
    display_surface.blit(dragon_left_image, dragon_left_rect)

    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (WINDOW_WIDTH, 75),4)

    pygame.display.update()

pygame.quit()                                                      