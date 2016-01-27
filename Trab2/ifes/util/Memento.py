__author__ = 'Bruno'
import copy


def Memento(obj, deep=False):
    state = (copy.copy, copy.deepcopy)[bool(deep)](obj.__dict__)
    def Restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return Restore