import pygame

pygame.init()#初始化pygame

WINDOW_WIDTH = 600#x
WINDOW_HELGHT = 300#Y

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HELGHT))

pygame.display.set_caption("Feed the Dragon!")

FPS = 60
clock = pygame.time.Clock()


dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.centerx = 300
dragon_left_rect.centery = 150

game_running = True
while game_running:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            game_running = False
        
    keys = pygame.key.get_pressed()
    print(keys)

    if keys[pygame.K_LEFT]:
        dragon_left_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        dragon_left_rect.x += 5
    if keys[pygame.K_UP]:
        dragon_left_rect.y -= 5
    if keys[pygame.K_DOWN]:
        dragon_left_rect.y += 5

    if dragon_left_rect.left < 0:
        dragon_left_rect.left = 0
    elif dragon_left_rect.right > WINDOW_WIDTH:
        dragon_left_rect.right = WINDOW_WIDTH
    if dragon_left_rect.top < 0:
        dragon_left_rect.top = 0
    elif dragon_left_rect.bottom > WINDOW_HELGHT:
        dragon_left_rect.bottom = WINDOW_HELGHT
    
        
    display_surface.fill((0,0,0))
    display_surface.blit(dragon_left_image, dragon_left_rect)
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()  
