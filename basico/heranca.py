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


class Carro(Transporte):
    def __init__(self, nome, peso, preco, precoSeguro):
        Transporte.__init__(self, nome, peso, preco)
        self.precoSeguro = precoSeguro
    
    def getPrecoSeguro(self):
        return self.precoSeguro

carro = Carro('Fusca', 300.78, 3500.00, 800)
print(carro.getNome())
print(carro.getPeso())
print(carro.getPeso())
print(carro.getPrecoSeguro())