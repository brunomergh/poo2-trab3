__author__ = 'Bruno'



from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaCadFornecedor:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[100,210],[80,210],[100,282],[100,354],[100,498],[150,500],[400,500]]
        self.ctrl = Control()
        self.listaCadastral =["","","","",""]

    def controle(self):
        self.teclado.capturaTeclas()


        TelaInicial,TelaCadastro = 2,3
        TelaCadFornecedor = 7

        name,fone,adress,cnpj = 0,1,2,3
        opcao = TelaCadFornecedor
        papelparede,nome, seta, tel, end, cpf, confirma, voltar = 0,1,2,3,4,5,6,7

        largura, altura = 0,1



        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[nome][altura]:

            self.posicao[seta][altura] -= 72


        elif self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[confirma][altura] -30:

            self.posicao[seta][altura] += 72


        if self.teclado.teclas[self.teclado.direita] and self.posicao[seta][altura]+2 == self.posicao[confirma][altura] and (self.posicao[seta][largura]+70) == self.posicao[confirma][largura]:
            self.posicao[seta][largura] += 240


        if self.teclado.teclas[self.teclado.esquerda] and self.posicao[seta][altura]+2 == self.posicao[voltar][altura] and (self.posicao[seta][largura]+80) == self.posicao[voltar][largura]:

            self.posicao[seta][largura] -= 240


        nome = (self.posicao[seta][altura] == self.posicao[nome][altura])
        tel = (self.posicao[seta][altura] == self.posicao[tel][altura])
        end = (self.posicao[seta][altura] == self.posicao[end][altura])
        cpf = (self.posicao[seta][altura] == self.posicao[cpf][altura])
        confirma = (self.posicao[seta][altura] == self.posicao[confirma][altura])
        voltar = (self.posicao[seta][largura]+80 == self.posicao[voltar][largura])

        if self.teclado.teclas[self.teclado.letra] != "":
            if nome:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[name])
                    self.pal=self.listaCadastral[name]
                    self.listaCadastral[name]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[name] += self.teclado.teclas[self.teclado.letra]

                return opcao, self.listaCadastral


            if tel:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[fone])
                    self.pal=self.listaCadastral[fone]
                    self.listaCadastral[fone]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[fone]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if end:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[adress])
                    self.pal=self.listaCadastral[adress]
                    self.listaCadastral[adress]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[adress]+=self.teclado.teclas[self.teclado.letra]
                return opcao, self.listaCadastral

            if cpf:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[cnpj])
                    self.pal=self.listaCadastral[cnpj]
                    self.listaCadastral[cnpj]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[cnpj]+=self.teclado.teclas[self.teclado.letra]
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
                self.ctrl.cad_fornecedor(self.listaCadastral)
                self.listaCadastral = ["","","","",""]
                self.posicao[seta][largura] = 80
                self.posicao[seta][altura] = 210
                return opcao,self.listaCadastral

        return opcao, self.listaCadastral