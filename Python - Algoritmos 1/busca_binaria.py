#LISTA
numeros = list()
tam = int(input("Tamanho do vetor: "))
for i in range(tam):
    valor = int(input(f"Digite o numero do vetor na posição {i}: "))
    numeros.append(valor)
print("Vetor: ", numeros)

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

#SELECTION SORT
for i in range(tam):
    indice_menor = i
    for j in range(int(i + 1), tam):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("vetor: ",numeros)

#BUSCA BINARIA

resultado = -1
inicio = 0
fim = tam - 1
meio = 0
alvo = int(input("Digite o elemento a ser encontrado: "))
while inicio <= fim:
    meio = int((inicio + fim) / 2)
    if (numeros[meio] < alvo):
        inicio = meio + 1
    elif (numeros[meio] > alvo):
        fim = meio - 1
    else:
        resultado = meio
        break
if resultado < 0:
    print("Elemento não encontrado")
else:
    print(f"O elemento {alvo} está na posição {resultado}")