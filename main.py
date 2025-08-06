import pygame 
from pygame.locals import *
import emitter


WINDOWHEIGHT = 800
WINDOWWIDTH = 800
FPS = 60
clock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
game_running = True

particle_group = pygame.sprite.Group()
basic_emitter = emitter.Emitter(5, particle_group)


BLACK = (0, 0, 0)
while game_running:

    DISPLAY.fill(BLACK)
    basic_emitter.update()    

    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

        if event.type == KEYDOWN:
            basic_emitter.setEmittingStatus(True)
            basic_emitter.request_amount(1)
    particle_group.update()
    particle_group.draw(DISPLAY)

    #print(particle_group)
    
    pygame.display.flip()
    clock.tick(FPS)

