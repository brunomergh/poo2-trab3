__author__ = 'Bruno'


from ifes.cih.imprimirNaJanela import ImprimirNaJanela


class TelaCadCompra:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.seta, self.ok, self.bvoltar= 0,2,7,8





    def imprime(self, janela,posicao,lstTexto):

        qtd, notaf, codfornec, codprod, dtcompra = 0,1,2,3,4
        pos = [[400,219],[400,289],[400,359],[400,429],[400,499]]
        texto_qtd = self.imprimi.fonte.render(lstTexto[qtd],1,(0,0,0))
        texto_notaf = self.imprimi.fonte.render(lstTexto[notaf],1,(0,0,0))
        texto_codfornec = self.imprimi.fonte.render(lstTexto[codfornec],1,(0,0,0))
        texto_codprod = self.imprimi.fonte.render(lstTexto[codprod],1,(0,0,0))
        texto_dtcompra = self.imprimi.fonte.render(lstTexto[dtcompra],1,(0,0,0))


        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeCadCompra.jpg",632,632)
        self.imprimi.imprime2(janela,pos[qtd],texto_qtd)
        self.imprimi.imprime2(janela,pos[notaf],texto_notaf)
        self.imprimi.imprime2(janela,pos[codfornec],texto_codfornec)
        self.imprimi.imprime2(janela,pos[codprod],texto_codprod)
        self.imprimi.imprime2(janela,pos[dtcompra],texto_dtcompra)
        self.imprimi.imprime(janela,self.posicao[self.ok],"bok.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.bvoltar],"bvoltar.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)