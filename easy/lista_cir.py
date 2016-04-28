import itertools
from time import sleep

class Lista:
    def __init__(self):
        self.lista = []

    def tamanho(self):
        return len(self.lista)

    def inserir(self, valor, pos):
        valor = int(valor)
        self.lista.insert(valor, pos)

    def remover(self, valor):
        self.lista.remove(valor)

    def __iter__(self):
        return iter(itertools.cycle(self.lista))

    def __repr__(self):
        return "{Lista}".format(Lista = self.lista)

"""
Testes
lista = Lista()
lista.inserir(0,0)
lista.inserir(1,1)
lista.inserir(2,2)

for x in lista:
    print x
    sleep(0.5)


print lista
"""
