class Transporte():
    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    def getNome(self):
        return self.nome

    def getPeso(self):
        return self.peso

    def getPreco(self):
        return self.preco

'''
class Carro(Transporte):
    def __init__(self, nome, preco, seguro, precoSeguro):
        Transporte
'''

t = Transporte('Fusca', 500, 3278.56)
print(t.getNome())
print(t.getNome())