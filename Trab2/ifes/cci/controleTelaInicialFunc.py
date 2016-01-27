__author__ = 'Bruno'

from ifes.cih.teclado import Teclado
from ifes.cci.control import Control
import pygame, sys

class ControleTelaInicialFunc:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[216,280],[144,280],[216,340]]
        self.ctrl = Control()


    def controle(self, listaCadastral):

        TelaInicialFunc,TelaCadastroFunc = 10,11

        self.teclado.capturaTeclas()

        opcao = TelaInicialFunc
        papelparede,bcadastrar, seta,  bsair = 0,1,2,3
        largura, altura = 0,1




        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[bcadastrar][altura]:

            self.posicao[seta][altura] -= 60

        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[bsair][altura]:

            self.posicao[seta][altura] += 60

        cadastrar = (self.posicao[seta][altura] == self.posicao[bcadastrar][altura])
        sair = (self.posicao[seta][altura] == self.posicao[bsair][altura])

        log = 0

        if self.teclado.teclas[self.teclado.enter]:
            if cadastrar :
                opcao = TelaCadastroFunc


            elif sair:

                pygame.quit()
                sys.exit()
        return opcao