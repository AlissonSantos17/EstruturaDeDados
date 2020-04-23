import abc

class Veiculo(abc.ABC):
    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0

    def __del__(self):
        print('O objeto foi removido da memoria.')

    @abc.abstractclassmethod
    def pintar(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    def abastecer(self, qtd_combustivel):
        self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            print('O veiculo já está ligado.')
        else:
            self.__is_ligado = True
            print('O veiculo foi ligado.')

    def desligar(self):
        if self.__is_ligado == False:
            print('O veiculo já está desligado.')
        else:
            self.__is_ligado == False

    def acelerar(self, velocidade=10):
        if self.__is_ligado == True:
            self.__velocidade += velocidade
        else:
            print('O veiculo precisa estar ligado para ser acelerado.')