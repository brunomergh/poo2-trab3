__author__ = 'Bruno'
import pygame,os


class ImprimirNaJanela:
    def __init__(self):
        self.fonte = pygame.font.SysFont("comicsansms",24)

    def imprime(self,janela,posicao,nome,x,y):
        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cci", "")
        self.file = os.path.join(diretorio, 'imagens', nome)
        self.imagem = pygame.image.load(self.file)
        self.imagem_redimensionada=pygame.transform.scale(self.imagem,(x,y))
        janela.screen.blit(self.imagem_redimensionada,posicao)

    def imprime2(self,janela,posicao,nome):
        file = os.path.split(os.path.abspath(__file__))[0]
        self.imagem = pygame.image.load(self.file)
        janela.screen.blit(nome,posicao)