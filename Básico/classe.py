#CRIANDO CLASSE PESSOA, E OBTENDO O NOME E A RESPECTIVA IDADE.
class Pessoa():
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def obterNome(self):
        return self.nome

    def obterIdade(self):
        return self.idade

p = Pessoa('Alisson', 19)

print(f'Nome: {p.obterNome()}')
print(f'Idade: {p.obterIdade()}')