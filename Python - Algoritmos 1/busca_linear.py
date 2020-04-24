#LISTA
numeros = list()
tam = int(input("Tamanho do vetor: "))
for i in range(tam):
    valor = int(input(f"Digite o numero do vetor na posição {i}: "))
    numeros.append(valor)

# BUSCA LINEAR
num_pesquisa = int(input("Número pesquisado: "))
posicao_resultado = -1

for i in range(tam):
    if numeros[i] == num_pesquisa:
        posicao_resultado = i
        break
if posicao_resultado < 0:
    print('Número não encontrado')
else:
    print(f"Número encontrado na posição {posicao_resultado}")
#FIM BUSCA LINEAR