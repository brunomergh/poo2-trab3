__author__ = 'Bruno'

from ifes.cci.controleTelaUpDate import *
from ifes.cci.controleTelaInicial import *
from ifes.cci.controleTelaCadastro import *
from ifes.cci.controleTelaRelatorio import *
from ifes.cci.controleTelaCadCliente import *
from ifes.cci.controleTelaCadProduto import *
from ifes.cci.controleTelaCadFornecedor import *
from ifes.cci.controleTelaCadVenda import *
from ifes.cci.controleTelaCadCompra import *
from ifes.cci.controleTelaLogin import *
from ifes.cci.controleTelaInicialFunc import *
from ifes.cci.controleTelaCadastroFunc import *
from ifes.cci.controleTelaRelatorioGerado import *

from ifes.cih.telaUpDate import TelaUpDate
from ifes.cih.TelaInicial import *
from ifes.cih.telaCadastro import *
from ifes.cih.telaRelatorio import *
from ifes.cih.telaCadCliente import *
from ifes.cih.telaCadProduto import *
from ifes.cih.telaCadFornecedor import *
from ifes.cih.telaCadVenda import *
from ifes.cih.telaCadCompra import *
from ifes.cih.telaLogin import *
from ifes.cih.telaInicialFunc import *
from ifes.cih.telaCadastroFunc import *
from ifes.cih.telaRelatorioGerado import *

class FlyweightFactory():

    def __init__(self):
        self.flys  = {}
        self.flys['TelaLogin'] = TelaLogin()
        self.flys['TelaUpdate'] = TelaUpDate()
        self.flys['TelaInicial'] = TelaInicial()
        self.flys['TelaInicialFunc'] = TelaInicialFunc()
        self.flys['TelaCadastro'] = TelaCadastro()
        self.flys['TelaCadastroFunc'] = TelaCadastroFunc()
        self.flys['TelaCadCliente'] = TelaCadCliente()
        self.flys['TelaCadFornecedor'] = TelaCadFornecedor()
        self.flys['TelaCadProduto'] = TelaCadProduto()
        self.flys['TelaCadCompra'] = TelaCadCompra()
        self.flys['TelaCadVenda'] = TelaCadVenda()
        self.flys['TelaRelatorio'] = TelaRelatorio()
        self.flys['TelaRelatorioGerado'] = TelaRelatorioGerado()

        self.flys['ControleTelaLogin'] = ControleTelaLogin()
        self.flys['ControleTelaUpdate'] = ControleTelaUpDate()
        self.flys['ControleTelaInicial'] = ControleTelaInicial()
        self.flys['ControleTelaInicialFunc'] = ControleTelaInicialFunc()
        self.flys['ControleTelaCadastro'] = ControleTelaCadastro()
        self.flys['ControleTelaCadastroFunc'] = ControleTelaCadastroFunc()
        self.flys['ControleTelaCadCliente'] = ControleTelaCadCliente()
        self.flys['ControleTelaCadFornecedor'] = ControleTelaCadFornecedor()
        self.flys['ControleTelaCadProduto'] = ControleTelaCadProduto()
        self.flys['ControleTelaCadCompra'] = ControleTelaCadCompra()
        self.flys['ControleTelaCadVenda'] = ControleTelaCadVenda()
        self.flys['ControleTelaRelatorio'] = ControleTelaRelatorio()
        self.flys['ControleTelaRelatorioGerado'] = ControleTelaRelatorioGerado()


    def FlyweightTela(self,nome):

        return self.flys[nome]