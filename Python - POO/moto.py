import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        print('O metodo foi chamado a partir da classe moto')
        self._qtd_combustivel += qtd_combustivel
        if self._qtd_combustivel >= 30:
            print('O tanque está cheio')
        else:
            self._qtd_combustivel +=qtd_combustivel
    def pintar(self, cor):
        if cor == 'azul' or cor == 'Azul':
            print('A moto não pode ser pintada de azul')
        else:
            self._cor = cor