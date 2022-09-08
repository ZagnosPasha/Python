import pygame
import time
import random

#set fonts up
pygame.font.init()

#window variables
WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Halo')


#load images
BACKGROUND = pygame.transform.scale(pygame.image.load('images\halo_background.jpg'),(WIDTH, HEIGHT))



def main_loop():
    framerate = 60
    timer = pygame.time.Clock()
    running = True
    level = 1
    lives = 4
    main_text = pygame.font.SysFont('freesansbold', 40, True, False)

    def update_window():
            WINDOW.blit(BACKGROUND, (0,0))
            lives_text = main_text.render(f'L I V E S: {lives}', True, (0,255,0))
            level_text = main_text.render(f'L E V E L: {level}', True, (0,255,0))
            WINDOW.blit(lives_text, (10,10))
            WINDOW.blit(level_text, (800,10))
            pygame.display.update()

    while running:
        timer.tick(framerate)
        update_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main_loop()