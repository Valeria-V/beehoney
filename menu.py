import pygame
from obj import Obj

class Menu:

    def __init__(self):

        self.bg = Obj("assets/start.bng", 0, 0)

        self.chance_scene = False

    def draw(self, window):
        self.bg.group.draw(window)

    def events(self, event):
        if event.type == pygame.KEYDOWN:  #se tecla pressionada
            if event.key == pygame.K_RETURN: #se tecla for enter
                self.chance_scene = True #chance_scene true, muda a cena