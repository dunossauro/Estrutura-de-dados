class Pilha:
    def __init__(self):
        self.pilha = []

    def tamanho(self):
        return len(self.pilha)

    def inserir(self, valor):
        valor = int(valor)
        self.pilha.append(valor)

    def remover(self):
        self.pilha.pop()

    def __iter__(self):
        return iter(self.pilha)

    def __repr__(self):
        return "{pilha}".format(pilha = self.pilha)
        
pilha = Pilha()
pilha.inserir(0)
pilha.inserir(1)
pilha.inserir(2)

for x in pilha:
    print x

print pilha

pilha.remover()
print pilha
