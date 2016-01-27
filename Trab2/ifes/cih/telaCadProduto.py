__author__ = 'Bruno'


from ifes.cih.imprimirNaJanela import ImprimirNaJanela


class TelaCadProduto:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.seta, self.ok, self.bvoltar= 0,2,7,8





    def imprime(self, janela,posicao,lstTexto):

        desc,estmin,qtdatual,custo,pctlucro = 0,1,2,3,4
        pos = [[400,219],[400,289],[400,359],[400,429],[400,499]]
        texto_desc = self.imprimi.fonte.render(lstTexto[desc],1,(0,0,0))
        texto_estmin = self.imprimi.fonte.render(lstTexto[estmin],1,(0,0,0))
        texto_qtdatual = self.imprimi.fonte.render(lstTexto[qtdatual],1,(0,0,0))
        texto_custo = self.imprimi.fonte.render(lstTexto[custo],1,(0,0,0))
        texto_pctlucro = self.imprimi.fonte.render(lstTexto[pctlucro],1,(0,0,0))


        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeCadProduto.png",632,632)
        self.imprimi.imprime2(janela,pos[desc],texto_desc)
        self.imprimi.imprime2(janela,pos[estmin],texto_estmin)
        self.imprimi.imprime2(janela,pos[qtdatual],texto_qtdatual)
        self.imprimi.imprime2(janela,pos[custo],texto_custo)
        self.imprimi.imprime2(janela,pos[pctlucro],texto_pctlucro)
        self.imprimi.imprime(janela,self.posicao[self.ok],"bok.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.bvoltar],"bvoltar.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)