import pygame
from obj import Obj


class Main:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True

        #self.start_screen = Obj("assets/start.png", 0, 0) #add objeto

    def draw(self):
        pass
        #self.start_screen.drawing(self.window) #desenha objeto

    def events(self):
        for events in pygame.event.get():  #para cada evento
            if events.type == pygame.QUIT: #verifica o tipo
                self.loop = False #executa acao

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()


game = Main(360, 640, "BeeHoney")
game.update()
