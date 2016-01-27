__author__ = 'Bruno'

from ifes.cih.imprimirNaJanela import ImprimirNaJanela

class TelaRelatorio:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.brapagar, self.seta, self.brareceber, self.brvendas, self.brestoque = 0,1,2,3,4,5



    def imprime(self, janela,posicao):

        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeRelatorio.png",632,632)
        self.imprimi.imprime(janela,self.posicao[self.brapagar],"brapagar.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.brareceber],"brareceber.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.brvendas],"brvendas.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.brestoque],"brestoque.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)