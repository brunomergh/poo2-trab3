__author__ = 'Bruno'


from ifes.cih.imprimirNaJanela import ImprimirNaJanela


class TelaCadFornecedor:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.seta, self.ok, self.bvoltar  = 0,2,6,7





    def imprime(self, janela,posicao,lstTexto):

        nome,tel,end,cpf = 0,1,2,3
        pos = [[300,219],[300,289],[300,359],[300,429],[300,499]]
        texto_nome = self.imprimi.fonte.render(lstTexto[nome],1,(0,0,0))
        texto_tel = self.imprimi.fonte.render(lstTexto[tel],1,(0,0,0))
        texto_end = self.imprimi.fonte.render(lstTexto[end],1,(0,0,0))
        texto_cpf = self.imprimi.fonte.render(lstTexto[cpf],1,(0,0,0))


        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeCadFornecedor.jpg",632,632)
        self.imprimi.imprime2(janela,pos[nome],texto_nome)
        self.imprimi.imprime2(janela,pos[tel],texto_tel)
        self.imprimi.imprime2(janela,pos[end],texto_end)
        self.imprimi.imprime2(janela,pos[cpf],texto_cpf)
        self.imprimi.imprime(janela,self.posicao[self.ok],"bok.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.bvoltar],"bvoltar.png",110,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)