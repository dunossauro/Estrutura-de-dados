class Fila:
    def __init__(self):
        self.fila = []

    def tamanho(self):
        return len(self.fila)

    def push(self, valor):
        valor = int(valor)
        self.fila.append(valor)

    def pop(self):
        self.fila.pop()

    def __iter__(self):
        return iter(self.fila)

    def __repr__(self):
        return "{fila}".format(fila = self.fila)
"""
Testes"""
fila = Fila()
fila.push(0)
fila.push(1)
fila.push(2)

fila.pop()

for x in fila:
    print(x)

print fila
"""
