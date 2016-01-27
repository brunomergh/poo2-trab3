__author__ = 'Bruno'

from ifes.cih.imprimirNaJanela import ImprimirNaJanela
class TelaInicialFunc:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.bcadastrar, self.seta, self.bsair = 0,1,2,3





    def imprime(self, janela,posicao):

        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeTelaInicial.jpg",632,632)
        self.imprimi.imprime(janela,self.posicao[self.bcadastrar],"bcadastrar.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.bsair],"bsair.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)

