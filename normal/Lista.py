import unittest

class Lista:
    class Noh:
        def __init__(self, element, _next=None, _back=None):
            self.elemento = element
            self.next = _next
            self.back = _back

    def __init__(self):
        self.cabeca = None
        self.calda = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def vazia(self):
        return self.tamanho == 0

    def inserir_dir(self, e):
        if self.vazia():
            self.cabeca = self.Noh(e)
            self.calda = self.cabeca
            self.tamanho += 1
        else:
            auxiliar = self.Noh(e)
            self.calda.next = auxiliar
            auxiliar.back = self.calda
            self.calda = auxiliar
            self.tamanho += 1

    def inserir_esq(self, e):
        if self.vazia():
            self.cabeca = self.Noh(e)
            self.calda = self.cabeca
            self.tamanho += 1
        else:
            auxiliar = self.Noh(e)
            auxiliar.next = self.cabeca
            self.cabeca.back = auxiliar
            self.cabeca = auxiliar
            self.tamanho += 1


    def remover_dir(self):
        if self.vazia():
            return None
        else:
            auxiliar = self.calda
            self.calda = self.calda.back
            self.tamanho -= 1
            del(auxiliar)

    def remover_esq(self):
        if self.vazia():
            return None
        else:
            auxiliar = self.cabeca.next
            self.cabeca = auxiliar
            self.tamanho -= 1

class Teste(unittest.TestCase):
    def teste_inserir_3_esq(self):
        lista = Lista()
        lista.inserir_esq(3)
        lista.inserir_esq(4)
        lista.inserir_esq(5)
        self.assertEqual(5, lista.cabeca.elemento)

    def teste_inserir_3_dir(self):
        lista = Lista()
        lista.inserir_dir(3)
        lista.inserir_dir(4)
        lista.inserir_dir(5)
        self.assertEqual(5, lista.calda.elemento)

    def teste_inserir_3_mix(self):
        lista = Lista()
        lista.inserir_dir(3)
        lista.inserir_esq(4)
        lista.inserir_dir(5)
        self.assertEqual(5, lista.calda.elemento)

    def teste_len(self):
        lista = Lista()
        valores = [1,2,3,4,5]

        for x in valores:
            lista.inserir_esq(x)

        self.assertEqual(len(valores),len(lista))

    def teste_cabeca(self):
        lista = Lista()
        self.assertIsNone(lista.cabeca)

    def teste_remover_null(self):
        lista = Lista()
        self.assertIsNone(lista.remover_esq())

    def teste_remover_dir(self):
        lista = Lista()
        lista.inserir_dir(3)
        lista.inserir_dir(4)
        lista.inserir_dir(5)
        lista.remover_dir()
        self.assertEqual(4, lista.calda.elemento)

    def teste_remover_esq(self):
        lista = Lista()
        lista.inserir_dir(3)
        lista.inserir_dir(4)
        lista.inserir_dir(5)
        lista.remover_esq()
        self.assertEqual(4, lista.cabeca.elemento)


if __name__ == '__main__':
    unittest.main()
