import unittest

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
            return None
        else:
            auxiliar = self.cabeca.elemento
            self.cabeca = self.cabeca.next
            self.tamanho -= 1
            return auxiliar

    def top(self):
        if self.vazia():
            return None
        else:
            return self.cabeca.elemento

class Teste(unittest.TestCase):
    def teste_pop(self):
        pilha = Pilha()
        pilha.push(3)
        self.assertEqual(3, pilha.pop())

    def teste_pop_null(self):
        pilha = Pilha()
        self.assertIsNone(pilha.pop())

    def teste_cabeca(self):
        pilha = Pilha()
        self.assertIsNone(pilha.cabeca)

    def teste_push(self):
        pilha = Pilha()
        pilha.push(3)
        self.assertEqual(pilha.cabeca.elemento, 3)

    def teste_len(self):
        pilha = Pilha()
        valores = [1,2,3,4,5]

        for x in valores:
            pilha.push(x)

        self.assertEqual(len(valores),len(pilha))

    def teste_top(self):
        pilha = Pilha()
        pilha.push(3)

        self.assertEqual(3,pilha.top())

if __name__ == '__main__':
    unittest.main()
