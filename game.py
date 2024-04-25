import pygame

pygame.init()#初始化pygame

WINDOW_WIDTH = 600#x
WINDOW_HELGHT = 300#Y

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HELGHT))

pygame.display.set_caption("Feed the Dragon!")


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

        if ev.type == pygame.MOUSEBUTTONDOWN:     
            print(ev)
            mouse_x = ev.pos[0]
            mouse_y = ev.pos[1]
            dragon_left_rect.centerx = mouse_x
            dragon_left_rect.centery = mouse_y
    
        if ev.type == pygame.MOUSEMOTION and ev.buttons[0] == 1:     
            print(ev)
            mouse_x = ev.pos[0]
            mouse_y = ev.pos[1]
            dragon_left_rect.centerx = mouse_x
            dragon_left_rect.centery = mouse_y

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_left_image, dragon_left_rect)

           
            


    
    
    pygame.display.update()

pygame.quit()  
