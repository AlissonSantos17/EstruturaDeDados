from vetores import vetor
from listas import lista_ligada
from listas import lista_duplamente_ligada

print(30 * "-", "MENU", 30 * "-")
print('1 - Vetores\n'
      '2 - Listas Ligadas\n'
      '3 - Listas Duplamente Ligadas\n')
menu = int(input('Digite a opção desejada: '))

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

elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    print(lista_teste.inserirPosicao(2, 10))
    print(lista_teste)
    lista_teste.removerElemento(4)
    print(lista_teste)

elif menu == 3:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    print(lista_teste.inserirPosicao(2, 10))
    print(lista_teste)
    # lista_teste.removerElemento(4)
    lista_teste.removerPosicao(1)
    print(lista_teste)