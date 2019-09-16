import pygame
import constants

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))

    def Prepare(self):
        self.screen.fill((255,255,255))

    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Circle(self,x,y):
        pygame.draw.circle(self.screen, (0,0,0), (x,y), 20, 0)
        
    def Draw_Line(self,x_base,y_base,x_tip,y_tip,width,color):
        pygame.draw.line(self.screen,color,(x_base,y_base),(x_tip,y_tip),width)
        
