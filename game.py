import pygame

pygame.init()#初始化pygame

WINDOW_WIDTH = 600#x
WINDOW_HELGHT = 300#Y

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HELGHT))

pygame.display.set_caption("Feed the Dragon!")
BLACK = (0,0,0)
White = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGNETA = (255,0,255)

display_surface.fill(BLUE)

pygame.draw.line(display_surface, RED, (0,0), (100,100), 10)
pygame.draw.line(display_surface, CYAN, (100,100), (300,300), 6)
pygame.draw.circle(display_surface, MAGNETA, (WINDOW_WIDTH // 2,WINDOW_HELGHT // 2), 100, 5)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH // 2,WINDOW_HELGHT // 2), 50, 0)



game_running = True
while game_running:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            game_running = False

    pygame.display.update()

pygame.quit()                                                      