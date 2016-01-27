__author__ = 'Bruno'

class FabricaGeral():

    @staticmethod
    def criar(nome):
        path = 'ifes.cdp.' + nome
        componentes = path.split('.')
        mod = __import__(componentes[0])
        for comp in componentes[1:]:
            mod = getattr(mod, comp)
        return mod

