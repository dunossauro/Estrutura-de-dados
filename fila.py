class Fila:
    def __init__(self):
        self.fila = []

    def tamanho(self):
        return len(self.fila)

    def inserir(self, valor):
        valor = int(valor)
        self.fila.append(valor)

    def remover(self):
        self.fila.pop()

    def __iter__(self):
        return iter(self.fila)

    def __repr__(self):
        return "{fila}".format(fila = self.fila)

fila = Fila()
fila.inserir(0)
fila.inserir(1)
fila.inserir(2)

fila.remover()

for x in fila:
    print(x)

print fila
