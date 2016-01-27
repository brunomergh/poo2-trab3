__author__ = 'Bruno'


__author__ = 'Bruno'


from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaRelatorio:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[216,220],[144,220],[216,280],[216,340],[216,400]]
        self.ctrl = Control()


    def controle(self):
        self.teclado.capturaTeclas()

        TelaRelatorio, TelaRelatorioGerado = 4, 12
        opcao = TelaRelatorio
        papelparede, brapagar, seta, brareceber, brvendas, brestoque = 0,1,2,3,4,5

        largura, altura = 0,1




        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[brapagar][altura]:

            self.posicao[seta][altura] -= 60

        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[brestoque][altura]:

            self.posicao[seta][altura] += 60

        brapagar = (self.posicao[seta][altura] == self.posicao[brapagar][altura])
        brareceber = (self.posicao[seta][altura] == self.posicao[brareceber][altura])
        brvendas = (self.posicao[seta][altura] == self.posicao[brvendas][altura])
        brestoque = (self.posicao[seta][altura] == self.posicao[brestoque][altura])

        if self.teclado.teclas[self.teclado.enter]:
            if brapagar:
                self.ctrl.gerar_relatorio_apagar()
                opcao = TelaRelatorioGerado


            elif brareceber:
                self.ctrl.gerar_relatorio_areceber()
                opcao = TelaRelatorioGerado


            elif brvendas:
                self.ctrl.gerar_relatorio_vendas()
                opcao = TelaRelatorioGerado


            elif brestoque:
                self.ctrl.gerar_relatorio_estoque()
                opcao = TelaRelatorioGerado


        return opcao