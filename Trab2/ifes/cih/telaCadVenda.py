__author__ = 'Bruno'


from ifes.cih.imprimirNaJanela import ImprimirNaJanela


class TelaCadVenda:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.seta, self.ok, self.bvoltar= 0,2,6,7





    def imprime(self, janela,posicao,lstTexto):

        cliente,dt,prod,qtd = 0,1,2,3
        pos = [[400,219],[400,289],[400,359],[400,429],[400,499]]
        texto_cliente = self.imprimi.fonte.render(lstTexto[cliente],1,(0,0,0))
        texto_dt = self.imprimi.fonte.render(lstTexto[dt],1,(0,0,0))
        texto_prod = self.imprimi.fonte.render(lstTexto[prod],1,(0,0,0))
        texto_qtd = self.imprimi.fonte.render(lstTexto[qtd],1,(0,0,0))


        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeCadVenda.jpg",632,632)
        self.imprimi.imprime2(janela,pos[cliente],texto_cliente)
        self.imprimi.imprime2(janela,pos[dt],texto_dt)
        self.imprimi.imprime2(janela,pos[prod],texto_prod)
        self.imprimi.imprime2(janela,pos[qtd],texto_qtd)
        self.imprimi.imprime(janela,self.posicao[self.ok],"bok.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.bvoltar],"bvoltar.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)