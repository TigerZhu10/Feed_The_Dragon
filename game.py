import pygame

pygame.init()#初始化pygame

WINDOW_WIDTH = 600
WINDOW_HELGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HELGHT))

pygame.display.set_caption("Feed the Dragon!")

game_running = True
while game_running:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            game_running = False

pygame.quit()