import pygame , sys

pygame.init()
WINDOW_WIDTH , WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

#importing images
ship_surf = pygame.image.load('C:/Users/USER/OneDrive/Desktop/python_projects/pygame_projects/pygame_project4/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))


#create a surface
bg_surf = pygame.image.load('C:/Users/USER/OneDrive/Desktop/python_projects/pygame_projects/pygame_project4/graphics/background.png').convert()

#import text
font_styles = 'C:/Users/USER/OneDrive/Desktop/python_projects/pygame_projects/pygame_project4/graphics/subatomic.ttf'

font = pygame.font.Font(font_styles,50)
text_surf = font.render('Space',True , (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOW_HEIGHT))



#keeps the code going
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()

    #framerate limit
    clock.tick(120)

    
        

    #updates
    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf,(0,0))
    
    #top of window
    if ship_rect.y >= 0:
        ship_rect.y -= 4
    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,text_rect)
    
    

    #frame rate/update display surface
    pygame.display.update()