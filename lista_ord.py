from bisect import bisect_left

class Lista:
    def __init__(self):
        self.lista = []

    def tamanho(self):
        return len(self.lista)

    def inserir(self, valor):
        valor = int(valor)
        pos = bisect_left(self.lista, valor)
        self.lista.insert(valor, pos)

    def remover(self, valor):
        self.lista.remove(valor)

    def __iter__(self):
        return iter(self.lista)

    def __repr__(self):
        return "{Lista}".format(Lista = self.lista)

lista = Lista()
lista.inserir(0)
lista.inserir(1)
lista.inserir(2)

print "Anter de inserir: {l}".format(l=lista)

lista.inserir(0)

print "Depois de inserir: {l}".format(l=lista)
