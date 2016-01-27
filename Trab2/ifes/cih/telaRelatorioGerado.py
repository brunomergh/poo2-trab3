__author__ = 'Bruno'

from ifes.cih.imprimirNaJanela import ImprimirNaJanela

class TelaRelatorioGerado:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede,self.seta, self.bvoltar= 0, 1, 2



    def imprime(self, janela,posicao):

        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeRelatorioGerado.png",632,632)
        self.imprimi.imprime(janela,self.posicao[self.bvoltar],"bvoltar.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)