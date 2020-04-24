numeros = list()

tam = int(input("Tamanho do vetor: "))

for i in range(tam):
    valor = int(input(f"Digite o numero do vetor na posição {i}: "))
    numeros.append(valor)
print(f"Vetor: {numeros}")
print(f"A posição 1 armazena o número {numeros[1]} ")