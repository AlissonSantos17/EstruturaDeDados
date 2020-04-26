from vetores import vetor

print(30 * "-", "MENU", 30 * "-")
print('1 - Vetores\n'
      '2 - Listas Ligadas\n'
      '3 - ?\n')
# menu = int(input('Digite a opção desejada: '))
menu = 1

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserirElemento(1, 0)
    vetor_teste.inserirElemento(2, 1)
    vetor_teste.inserirElemento(3, 2)
    vetor_teste.inserirElemento(4, 2)
    vetor_teste.inserirElemento(5, 2)
    vetor_teste.inserirElementoFinal(1)
    print(f'Vetor: {vetor_teste}')
    vetor_teste.removerElementoIndice(3)
    print('Tamanho do vetor', vetor_teste.tamanhoVetor())
    print('Indice: ', vetor_teste.indice(3))
    print(f'Vetor: {vetor_teste}')
    vetor_teste.removerElemento(5)
    print(f'Vetor: {vetor_teste}')
