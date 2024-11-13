import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT +1
BACKGROUND_COLOR_CHANGE_EVENT =
pygame.USEREVENT + 2

BLUE = pygame.COLOR('blue')
LIGHTBLUE = pygame.COLOR('lightblue')
DARKBLUE = pygame.COLOR('darkblue')

YELLOW = pygame.COLOR('yellow')
MAGENTA = pygame.COLOR('magenta')
ORANGE = pygame.COLOR('orange')
WHITE = pygame.COLOR('white')

class Sprite(pygame.spirite.Sprite):

    def __init__(self, color, hieght, width):

        super().__init__()

        self.image = pygame.Surface([width, hieght])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity =[random.choice([-1, 1]),random.choice([-1, 1])] 
    
    def update(self):

        self.rect.move_ip(self.velocity)

        boundary_hit = False

        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity

