import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        """Inatilise the alien and set it's sstarting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store Alien's exact horizonral position
        self.x = float(self.rect.x)
