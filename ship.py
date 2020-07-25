import pygame

class Ship:
    """ A class to manage the ship"""

    def __init__(self, ai_game):

        """Initialise the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get it rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""

        #update the ship's value not the rect

        if self.moving_right and self.rect.right < self.screen_rect.right:

        #if self.moving_right:
           self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
           #self.rect.x += 1 #can be remove
            if self.moving_left:
                self.x -= self.settings.ship_speed

            #update rect object form self.x

            #self.rect.x -= 1
        self.rect.x = self.x 
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)