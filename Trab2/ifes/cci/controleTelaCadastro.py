__author__ = 'Bruno'


from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaCadastro:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[216,230],[144,230],[216,290],[216,350],[216,410],[216,470],[216,530]]
        self.ctrl = Control()


    def controle(self,listacadastral):
        self.teclado.capturaTeclas()


        TelaInicial, TelaCadastro, TelaCadCliente, TelaCadProduto, TelaCadFornecedor, TelaCadCompra, TelaCadVenda = 2,3,5,6,7,8,9
        opcao = TelaCadastro
        papelparede,bccliente, seta, bcproduto, bcfornecedor, bccompra, bcvenda, bvoltar = 0,1,2,3,4,5,6,7

        largura, altura = 0,1

        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[bccliente][altura]:

            self.posicao[seta][altura] -= 60

        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[bvoltar][altura]:

            self.posicao[seta][altura] += 60

        bccliente = (self.posicao[seta][altura] == self.posicao[bccliente][altura])
        bcproduto = (self.posicao[seta][altura] == self.posicao[bcproduto][altura])
        bcfornecedor = (self.posicao[seta][altura] == self.posicao[bcfornecedor][altura])
        bccompra = (self.posicao[seta][altura] == self.posicao[bccompra][altura])
        bcvenda = (self.posicao[seta][altura] == self.posicao[bcvenda][altura])
        bvoltar = (self.posicao[seta][altura] == self.posicao[bvoltar][altura])

        if self.teclado.teclas[self.teclado.enter]:
            if bccliente:
                opcao = TelaCadCliente
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230

            elif bcproduto:
                opcao = TelaCadProduto
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230


            elif bcfornecedor:
                opcao = TelaCadFornecedor
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230


            elif bccompra:
                opcao = TelaCadCompra
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230


            elif bcvenda:
                opcao = TelaCadVenda
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230


            elif bvoltar:
                opcao = TelaInicial
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230


        return opcao, listacadastral