__author__ = 'Bruno'

from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaCadCompra:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[100,210],[80,210],[100,282],[100,354],[100,426],[100,498],[150,570],[400,570]]
        self.ctrl = Control()
        self.listaCadastral =["","","","",""]

    def controle(self):
        self.teclado.capturaTeclas()

        TelaInicial,TelaCadastro = 2,3
        TelaCadCompra = 8

        quantity,notafisc,codefornec,codeprod,date = 0,1,2,3,4
        opcao = TelaCadCompra
        papelparede,qtd,seta,notaf,codfornec,codprod,dtcompra,confirma, voltar= 0,1,2,3,4,5,6,7,8

        largura, altura = 0,1




        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[qtd][altura]:

            self.posicao[seta][altura] -= 72


        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[confirma][altura]:

            self.posicao[seta][altura] += 72

        if self.teclado.teclas[self.teclado.direita] and self.posicao[seta][altura] == self.posicao[confirma][altura] and (self.posicao[seta][largura]+70) == self.posicao[confirma][largura]:
            self.posicao[seta][largura] += 240


        if self.teclado.teclas[self.teclado.esquerda] and self.posicao[seta][altura] == self.posicao[voltar][altura] and (self.posicao[seta][largura]+80) == self.posicao[voltar][largura]:

            self.posicao[seta][largura] -= 240



        qtd = (self.posicao[seta][altura] == self.posicao[qtd][altura])
        notaf = (self.posicao[seta][altura] == self.posicao[notaf][altura])
        codfornec = (self.posicao[seta][altura] == self.posicao[codfornec][altura])
        codprod = (self.posicao[seta][altura] == self.posicao[codprod][altura])
        dtcompra = (self.posicao[seta][altura] == self.posicao[dtcompra][altura])
        confirma = (self.posicao[seta][altura] == self.posicao[confirma][altura])
        voltar = (self.posicao[seta][largura]+80 == self.posicao[voltar][largura])

        if self.teclado.teclas[self.teclado.letra] != "":
            if qtd:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[quantity])
                    self.pal=self.listaCadastral[quantity]
                    self.listaCadastral[quantity]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[quantity] += self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral


            if notaf:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[notafisc])
                    self.pal=self.listaCadastral[notafisc]
                    self.listaCadastral[notafisc]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[notafisc]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if codfornec:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[codefornec])
                    self.pal=self.listaCadastral[codefornec]
                    self.listaCadastral[codefornec]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[codefornec]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if codprod:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[codeprod])
                    self.pal=self.listaCadastral[codeprod]
                    self.listaCadastral[codeprod]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[codeprod]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if dtcompra:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[date])
                    self.pal=self.listaCadastral[date]
                    self.listaCadastral[date]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[date]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

        if self.teclado.teclas[self.teclado.enter]:
            if voltar:
                opcao = TelaCadastro
                self.posicao[seta][largura] = 80
                self.posicao[seta][altura] = 210
                self.listaCadastral = ["","","","",""]
                return opcao,self.listaCadastral
            elif confirma:
                opcao = TelaInicial
                self.ctrl.cad_compra(self.listaCadastral)
                self.listaCadastral = ["","","","",""]
                self.posicao[seta][largura] = 80
                self.posicao[seta][altura] = 210
                return opcao,self.listaCadastral

            return opcao, self.listaCadastral