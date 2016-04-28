class Pilha:

    class Noh:
        def __init__(self, element, next):
            self.elemento = element
            self.next = next

    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def vazia(self):
        return self.tamanho == 0

    def push(self, e):
        self.cabeca = self.Noh(e, self.cabeca)
        self.tamanho += 1

    def pop(self):
        if self.vazia():
            raise "Lista Vazia"

        auxiliar = self.cabeca.elemento
        self.cabeca = self.cabeca.next
        self.size -= 1
        return auxiliar

    def top(self):
        if self.vazia():
            raise "Lista Vazia"

        return self.cabeca.elemento
