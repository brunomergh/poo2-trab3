__author__ = 'Bruno'

from ifes.cih.criarJanela import CriaJanela
import pygame
from ifes.util.flyweightFactory import FlyweightFactory


class Tela:

    def gerencia(self):


        pygame.init()
        pygame.key.set_repeat(0)
        tela = ""
        controle = ""




        janela=CriaJanela()


        main_clock=pygame.time.Clock()

        listaCadastral = []

        TelaLogin,TelaUpdate,TelaInicial,TelaCadastro,TelaRelatorio,TelaCadCliente,TelaCadProduto = 0,1,2,3,4,5,6
        TelaCadFornecedor,TelaCadCompra,TelaCadVenda,TelaInicialFunc,TelaCadastroFunc,TelaRelatorioGerado = 7,8,9,10,11,12
        opcao = TelaLogin

        flyfactory = FlyweightFactory()

        while True:

            janela.screen.fill(0)
            main_clock.tick(8)

            if opcao == TelaLogin:
                if str(type(tela)) != "<class 'ifes.cih.telaLogin.TelaLogin'>":
                    tela = flyfactory.FlyweightTela('TelaLogin')
                    controle = flyfactory.FlyweightTela('ControleTelaLogin')
                opcao, listaCadastral = controle.controle()
                tela.imprime(janela,controle.posicao, listaCadastral)

            if opcao == TelaUpdate:
                if str(type(tela)) != "<class 'ifes.cih.telaUpDate.TelaUpdate'>":
                    tela = flyfactory.FlyweightTela('TelaUpdate')
                    controle = flyfactory.FlyweightTela('ControleTelaUpdate')
                opcao = controle.controle()
                tela.imprime(janela,controle.posicao)


            if opcao == TelaInicial:
                if str(type(tela)) != "<class 'ifes.cih.telaInicial.TelaInicial'>":
                    tela = flyfactory.FlyweightTela('TelaInicial')
                    controle = flyfactory.FlyweightTela('ControleTelaInicial')
                opcao,listaCadastral = controle.controle(listaCadastral)
                tela.imprime(janela,controle.posicao)


            if opcao == TelaCadastro:
                if str(type(tela)) != "<class 'ifes.cih.telaCadastro.TelaCadastro'>":
                    tela = flyfactory.FlyweightTela('TelaCadastro')
                    controle = flyfactory.FlyweightTela('ControleTelaCadastro')
                opcao, listaCadastral = controle.controle(listaCadastral)
                tela.imprime(janela,controle.posicao)


            if opcao == TelaRelatorio:
                if str(type(tela)) != "<class 'ifes.cih.telaRelatorio.TelaRelatorio'>":
                    tela = flyfactory.FlyweightTela('TelaRelatorio')
                    controle = flyfactory.FlyweightTela('ControleTelaRelatorio')
                opcao = controle.controle()
                tela.imprime(janela,controle.posicao)


            if opcao == TelaCadCliente:
                if str(type(tela)) != "<class 'ifes.cih.telaCadCliente.TelaCadCliente'>":
                    tela = flyfactory.FlyweightTela('TelaCadCliente')
                    controle = flyfactory.FlyweightTela('ControleTelaCadCliente')
                opcao,listaCadastral = controle.controle(listaCadastral)
                tela.imprime(janela,controle.posicao,listaCadastral)


            if opcao == TelaCadProduto:
                if str(type(tela)) != "<class 'ifes.cih.telaCadProduto.TelaCadProduto'>":
                    tela = flyfactory.FlyweightTela('TelaCadProduto')
                    controle = flyfactory.FlyweightTela('ControleTelaCadProduto')
                opcao,listaCadastral = controle.controle()
                tela.imprime(janela,controle.posicao,listaCadastral)


            if opcao == TelaCadFornecedor:
                if str(type(tela)) != "<class 'ifes.cih.telaCadFornecedor.TelaCadFornecedor'>":
                    tela = flyfactory.FlyweightTela('TelaCadFornecedor')
                    controle = flyfactory.FlyweightTela('ControleTelaCadFornecedor')
                opcao,listaCadastral = controle.controle()
                tela.imprime(janela,controle.posicao,listaCadastral)

            if opcao == TelaCadCompra:
                if str(type(tela)) != "<class 'ifes.cih.telaCadCompra.TelaCadCompra'>":
                    tela = flyfactory.FlyweightTela('TelaCadCompra')
                    controle = flyfactory.FlyweightTela('ControleTelaCadCompra')
                opcao,listaCadastral = controle.controle()
                tela.imprime(janela,controle.posicao,listaCadastral)


            if opcao == TelaCadVenda:
               if str(type(tela)) != "<class 'ifes.cih.telaCadVenda.TelaCadVenda'>":
                    tela = flyfactory.FlyweightTela('TelaCadVenda')
                    controle = flyfactory.FlyweightTela('ControleTelaCadVenda')
               opcao,listaCadastral = controle.controle(listaCadastral)
               tela.imprime(janela,controle.posicao,listaCadastral)


            if opcao == TelaInicialFunc:
                if str(type(tela)) != "<class 'ifes.cih.telaInicialFunc.TelaInicialFunc'>":
                    tela = flyfactory.FlyweightTela('TelaInicialFunc')
                    controle = flyfactory.FlyweightTela('ControleTelaInicialFunc')
                opcao = controle.controle(listaCadastral)
                tela.imprime(janela,controle.posicao)



            if opcao == TelaCadastroFunc:
                if str(type(tela)) != "<class 'ifes.cih.telaCadastroFunc.TelaCadastroFunc'>":
                    tela = flyfactory.FlyweightTela('TelaCadastroFunc')
                    controle = flyfactory.FlyweightTela('ControleTelaCadastroFunc')
                opcao = controle.controle()
                tela.imprime(janela,controle.posicao)

            if opcao == TelaRelatorioGerado:
                if str(type(tela)) != "<class 'ifes.cih.telaRelatorioGerado.TelaRelatorioGerado'>":
                    tela = flyfactory.FlyweightTela('TelaRelatorioGerado')
                    controle = flyfactory.FlyweightTela('ControleTelaRelatorioGerado')
                opcao = controle.controle()
                tela.imprime(janela,controle.posicao)


            pygame.display.update()

