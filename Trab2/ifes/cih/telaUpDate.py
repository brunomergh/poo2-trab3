__author__ = 'Bruno'

from ifes.cih.imprimirNaJanela import ImprimirNaJanela

class TelaUpDate:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.bsim, self.seta, self.bnao = 0,1,2,3





    def imprime(self, janela,posicao):

        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeUpDate.jpg",632,632)
        self.imprimi.imprime(janela,self.posicao[self.bsim],"bsim.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.bnao],"bnao.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)