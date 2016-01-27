__author__ = 'Bruno'

from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaCadProduto:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[100,210],[80,210],[100,282],[100,354],[100,426],[100,498],[150,570],[400,570]]
        self.ctrl = Control()
        self.listaCadastral =["","","","",""]

    def controle(self):
        self.teclado.capturaTeclas()

        TelaInicial,TelaCadastro = 2,3
        TelaCadProduto = 6

        name,min,atual,price,lucro = 0,1,2,3,4
        opcao = TelaCadProduto
        papelparede,desc,seta,estmin,qtdatual,custo,pctlucro,confirma, voltar= 0,1,2,3,4,5,6,7,8

        largura, altura = 0,1




        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[desc][altura]:

            self.posicao[seta][altura] -= 72


        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[confirma][altura]:

            self.posicao[seta][altura] += 72

        if self.teclado.teclas[self.teclado.direita] and self.posicao[seta][altura] == self.posicao[confirma][altura] and (self.posicao[seta][largura]+70) == self.posicao[confirma][largura]:
            self.posicao[seta][largura] += 240


        if self.teclado.teclas[self.teclado.esquerda] and self.posicao[seta][altura] == self.posicao[voltar][altura] and (self.posicao[seta][largura]+80) == self.posicao[voltar][largura]:

            self.posicao[seta][largura] -= 240



        desc = (self.posicao[seta][altura] == self.posicao[desc][altura])
        estmin = (self.posicao[seta][altura] == self.posicao[estmin][altura])
        qtdatual = (self.posicao[seta][altura] == self.posicao[qtdatual][altura])
        custo = (self.posicao[seta][altura] == self.posicao[custo][altura])
        pctlucro = (self.posicao[seta][altura] == self.posicao[pctlucro][altura])
        confirma = (self.posicao[seta][altura] == self.posicao[confirma][altura])
        voltar = (self.posicao[seta][largura]+80 == self.posicao[voltar][largura])

        if self.teclado.teclas[self.teclado.letra] != "":
            if desc:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[name])
                    self.pal=self.listaCadastral[name]
                    self.listaCadastral[name]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[name] += self.teclado.teclas[self.teclado.letra]

                return opcao, self.listaCadastral


            if estmin:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[min])
                    self.pal=self.listaCadastral[min]
                    self.listaCadastral[min]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[min]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if qtdatual:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[atual])
                    self.pal=self.listaCadastral[atual]
                    self.listaCadastral[atual]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[atual]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if custo:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[price])
                    self.pal=self.listaCadastral[price]
                    self.listaCadastral[price]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[price]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if pctlucro:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[lucro])
                    self.pal=self.listaCadastral[lucro]
                    self.listaCadastral[lucro]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[lucro]+=self.teclado.teclas[self.teclado.letra]
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
                self.ctrl.cad_produto(self.listaCadastral)
                self.listaCadastral = ["","","","",""]
                self.posicao[seta][largura] = 80
                self.posicao[seta][altura] = 210
                return opcao,self.listaCadastral

        return opcao, self.listaCadastral