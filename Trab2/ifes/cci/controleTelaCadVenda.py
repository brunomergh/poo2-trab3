__author__ = 'Bruno'

from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaCadVenda:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[100,210],[80,210],[100,282],[100,354],[100,426],[150,498],[400,498]]
        self.ctrl = Control()
        self.listaCadastral =["","","","",""]

    def controle(self, listaCadastral):
        self.teclado.capturaTeclas()

        TelaInicial,TelaCadastro = 2,3
        TelaCadVenda, TelaCadastroFunc = 9, 11

        cli,data,pro,quant = 0,1,2,3
        opcao = TelaCadVenda
        papelparede,cliente,seta,dt,prod,qtd,confirma, voltar= 0,1,2,3,4,5,6,7

        largura, altura = 0,1




        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[cliente][altura]:

            self.posicao[seta][altura] -= 72


        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[confirma][altura]:

            self.posicao[seta][altura] += 72


        if self.teclado.teclas[self.teclado.direita] and self.posicao[seta][altura] == self.posicao[confirma][altura] and (self.posicao[seta][largura]+70) == self.posicao[confirma][largura]:
            self.posicao[seta][largura] += 240


        if self.teclado.teclas[self.teclado.esquerda] and self.posicao[seta][altura] == self.posicao[voltar][altura] and (self.posicao[seta][largura]+80) == self.posicao[voltar][largura]:

            self.posicao[seta][largura] -= 240



        cliente = (self.posicao[seta][altura] == self.posicao[cliente][altura])
        dt = (self.posicao[seta][altura] == self.posicao[dt][altura])
        prod = (self.posicao[seta][altura] == self.posicao[prod][altura])
        qtd = (self.posicao[seta][altura] == self.posicao[qtd][altura])
        confirma = (self.posicao[seta][altura] == self.posicao[confirma][altura])
        voltar = (self.posicao[seta][largura]+80 == self.posicao[voltar][largura])

        if self.teclado.teclas[self.teclado.letra] != "":
            if cliente:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[cli])
                    self.pal=self.listaCadastral[cli]
                    self.listaCadastral[cli]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[cli] += self.teclado.teclas[self.teclado.letra]

                return opcao, self.listaCadastral


            if dt:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[data])
                    self.pal=self.listaCadastral[data]
                    self.listaCadastral[data]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[data]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if prod:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[pro])
                    self.pal=self.listaCadastral[pro]
                    self.listaCadastral[pro]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[pro]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if qtd:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[quant])
                    self.pal=self.listaCadastral[quant]
                    self.listaCadastral[quant]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[quant]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

        log = 0

        if self.teclado.teclas[self.teclado.enter]:
            if voltar and listaCadastral[log] == "admin":
                opcao = TelaCadastro
                self.posicao[seta][largura] = 80
                self.posicao[seta][altura] = 210
                self.listaCadastral = ["","","","",""]
                return opcao,self.listaCadastral
            elif voltar:
                opcao = TelaCadastroFunc
                self.posicao[seta][largura] = 80
                self.posicao[seta][altura] = 210
                self.listaCadastral = ["","","","",""]
                return opcao,self.listaCadastral
            elif confirma:
                opcao = TelaInicial
                self.ctrl.cad_venda(self.listaCadastral)
                self.listaCadastral = ["","","","",""]
                self.posicao[seta][largura] = 80
                self.posicao[seta][altura] = 210
                return opcao,self.listaCadastral

        return opcao, self.listaCadastral