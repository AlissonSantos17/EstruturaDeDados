from .no import No

class ListaLigada():
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__tamanho = 0

    def inserir(self, elemento):
        novo_no = No(elemento)
        if self.estaVazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        self.__tamanho += 1

    def inserirPosicao(self, posicao, elemento):
        if posicao == 0:
            novo_no = No(elemento)
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no = novo_no
        elif posicao == self.__tamanho:
            novo_no = No(elemento)
            self.__ultimo_no.proximo = novo_no
            self.__ultimo_no = novo_no
        else:
            no_anterior = self.recuperarNo(posicao - 1)
            no_atual = self.recuperarNo(posicao)
            novo_no = No(elemento)
            no_anterior.proximo = novo_no
            novo_no.proximo = no_atual
        self.__tamanho += 1

    def contem(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperarNo(i)
            if no_atual.elemento == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperarNo(i)
            if no_atual.elemento == elemento:
                return i
        return -1

    def estaVazia(self):
        return self.__tamanho == 0

    def __str__(self):
        no = self.__primeiro_no
        elementos = ''
        for i in range(self.__tamanho):
            elementos = f'{elementos}{no.elemento} '
            no = no.proximo
        return elementos

    def recuperarElementoNo(self, posicao):
        no = self.recuperarNo(posicao)
        if no != None:
            return no.elemento
        return None

    def recuperarNo(self, posicao):
        resultado = 0
        for i in range(posicao + 1):
            if i == 0:
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximo
        return resultado

    def removerElemento(self, elemento):
        no_remover = self.indice(elemento)
        if no_remover == -1:
            print('Elemento não existe')
        self.removerPosicao(no_remover)

    def removerPosicao(self, posicao):
        if posicao == 0:
            proximo_no = self.__primeiro_no.proximo
            self.__primeiro_no = None
            self.__primeiro_no = proximo_no
        elif posicao == self.__tamanho - 1:
            penultimo_no = self.recuperarNo(self.__tamanho - 2)
            penultimo_no.proximo = None
            self.__ultimo_no = penultimo_no
        else:
            no_remover = self.recuperarNo(posicao)
            no_anterior = self.recuperarNo(posicao - 1)
            no_anterior.proximo = no_remover.proximo
            no_remover.proximo = None
        self.__tamanho -= 1