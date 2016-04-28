import heapq

class Fila:
    def __init__(self):
        self.fila = []

    def tamanho(self):
        return len(self.fila)

    def push(self, valor, prioridade):
        valor = int(valor)
        heapq.heappush(self.fila, (prioridade, valor))

    def pop(self):
        heapq.heappop(self.fila)[-1]

    def __iter__(self):
        return iter(self.fila)

    def __repr__(self):
        return "{fila}".format(fila = self.fila)

"""
Testes
fila = Fila()
fila.push(0,2)
fila.push(1,1)
fila.push(2,0)

print fila

fila.pop()
print fila

fila.pop()

print fila
"""
