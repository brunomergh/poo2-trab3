__author__ = 'Bruno'

import pygame, sys, os

class CriaJanela:
    def __init__(self):
        if sys.platform == 'win32' or sys.platform == 'win64':  #SE FOR WINDOWS 32 OU 64
            os.environ['SDL_VIDEO_CENTERED'] = '1' #DEFINE CENTRO

        self.screen=pygame.display.set_mode((632,632)) #Tamanho da janela (largura,altura)
        pygame.display.set_caption("trabalho poo") #Nome da janela "string"