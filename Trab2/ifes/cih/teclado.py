__author__ = 'Bruno'

import pygame,sys


class Teclado:
    def __init__(self):


        self.teclas=[False,False,False,False,False,""]
        self.cima,self.baixo,self.enter,self.direita, self.esquerda, self.letra = 0,1,2,3,4,5

    def capturaTeclas(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.teclas[self.cima]=True
                if event.key == pygame.K_DOWN:
                    self.teclas[self.baixo]=True
                if event.key == pygame.K_RETURN:
                    self.teclas[self.enter]=True
                if event.key == pygame.K_RIGHT:
                    self.teclas[self.direita] = True
                if event.key == pygame.K_LEFT:
                    self.teclas[self.esquerda] = True
                if (event.key >= 33 and event.key<=126) or (event.key == 8) or (event.key == 32):
                    self.teclas[self.letra]=chr(event.key)



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.teclas[self.cima]=False
                if event.key == pygame.K_DOWN:
                    self.teclas[self.baixo]=False
                if event.key == pygame.K_RETURN:
                    self.teclas[self.enter]=False
                if event.key == pygame.K_RIGHT:
                    self.teclas[self.direita] = False
                if event.key == pygame.K_LEFT:
                    self.teclas[self.esquerda] = False
                if (event.key >= 33 and event.key<=126)or (event.key == 8) or (event.key == 32):
                    self.teclas[self.letra]=""

