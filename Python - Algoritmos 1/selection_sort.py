#SELECTION SORT
numeros = list()
tam = int(input("Tamanho do vetor: "))
for i in range(tam):
    valor = int(input(f"Digite o numero do vetor na posição {i}: "))
    numeros.append(valor)

for i in range(tam):
    indice_menor = i
    for j in range(int(i + 1), tam):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("vetor: ",numeros)