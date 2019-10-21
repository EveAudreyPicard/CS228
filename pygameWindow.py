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
        
    def Draw_Black_Line(self,x_base,y_base,x_tip,y_tip,width):
        pygame.draw.line(self.screen,(0,0,0),(x_base,y_base),(x_tip,y_tip),width)

    def DrawImageToHelpUserPutTheirHandOverTheDevice(self,x,y,image_name):
        hand_wave = pygame.image.load(image_name)
        hand_wave = pygame.transform.scale(hand_wave,(constants.pygameWindowWidth/2,constants.pygameWindowDepth/2))
        self.screen.blit(hand_wave,(x,y))

    def Draw_Leap_Device(self,x,y,image_name):
        leap_device = pygame.image.load(image_name)
        leap_device = pygame.transform.scale(leap_device,(constants.pygameWindowWidth/3,constants.pygameWindowDepth/5))
        self.screen.blit(leap_device,(x,y))
        
    def Draw_Seconds(self,x,y,image_name):
        Second = pygame.image.load(image_name)
        Second = pygame.transform.scale(Second,(constants.pygameWindowWidth/3,constants.pygameWindowDepth/5))
        self.screen.blit(Second,(x,y))

    def Draw_Hand_Direction(self,x,y,image_name):
        hand_dir = pygame.image.load(image_name)
        hand_dir = pygame.transform.scale(hand_dir,(constants.pygameWindowWidth/4,constants.pygameWindowDepth/4))
        self.screen.blit(hand_dir,(x,y))

    def Draw_ASL_sign(self,x,y,image_name):
        asl_sign = pygame.image.load(image_name)
        asl_sign = pygame.transform.scale(asl_sign,(constants.pygameWindowWidth/2,constants.pygameWindowDepth/2))
        self.screen.blit(asl_sign,(x,y))

    def Draw_digit(self,x,y,image_name):
        digit = pygame.image.load(image_name)
        digit = pygame.transform.scale(digit,(constants.pygameWindowWidth/2,constants.pygameWindowDepth/2))
        self.screen.blit(digit,(x,y))

            
