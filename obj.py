import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()  #add grupo ao Obj
        self.sprite = pygame.sprite.Sprite(self.group) #add Sprite ao Obj

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

    def drawing(self, window):
        self.group.draw(window)
        #window.blit(self.image, (self.rect[0], self.rect[1]))
