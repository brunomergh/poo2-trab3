__author__ = 'Bruno'

from ifes.cih.imprimirNaJanela import ImprimirNaJanela
class TelaLogin:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.seta, self.confirma= 0, 2, 4





    def imprime(self, janela, posicao, lstTexto):

        self.posicao = posicao
        login,senha = 0,1
        pos = [[310,300],[310,360]]
        texto_login = self.imprimi.fonte.render(lstTexto[login],1,(0,0,0))
        texto_senha = self.imprimi.fonte.render(lstTexto[senha],1,(0,0,0))
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeLogin.png",632,632)
        self.imprimi.imprime2(janela,pos[login],texto_login)
        self.imprimi.imprime2(janela,pos[senha],texto_senha)
        self.imprimi.imprime(janela,self.posicao[self.confirma],"bok.png",70,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)

