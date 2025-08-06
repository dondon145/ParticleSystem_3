import pygame
import math

BLUE = (0, 0, 255)

class Particle(pygame.sprite.Sprite):
    
    def die(self):
        if self.life < 0:
            self.kill()

    def change_position(self):
        self.pos_x += self.vel_x
        self.pos_y -= self.vel_y

    def set_rect_center(self):
        self.rect.center = (self.pos_x, self.pos_y)

    def decrease_life(self, val):
        self.life -= val


    def update(self):

        self.die()
        self.decrease_life(1/60)
        self.change_position()
        self.set_rect_center()

    def __init__(self, width, height, pos_x, pos_y, color, speed, x_angle, y_angle, life):
        super().__init__()
        self.vel_x = speed* math.cos(x_angle* math.pi/180)
        self.vel_y = speed* math.sin(y_angle* math.pi/180)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.life = life

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)