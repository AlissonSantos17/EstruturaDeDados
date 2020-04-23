from usuario import Usuario

continuar = 1
user_list = []

while continuar != 0:
  try:
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    sobrenome = input('Digite seu sobrenome: ')

    usuario = Usuario(nome, idade, sobrenome)
    user_list.append(usuario)

    if(usuario.idade == 99):
      break
    if(usuario.idade == 98):
      continue

    print(f'Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}')

    if(usuario.idade <= 17):
      print(f'{usuario.nome } é adolecente')
    elif (usuario.idade >= 18 and usuario.idade <= 50):
      print(f'{usuario.nome} é adulto')
    else:
      print(f'{usuario.nome} é idoso')

    continuar = int(input('Deseja continuar? 0 - Sair | 1 - Continuar: '))
  except ValueError:
    print('Você deve informar um número válido!')
    

else:
  print(f'Lista de usúarios cadastrados: ')
  
  for x in user_list:
    print(f'Nome completo: {x.nome} {x.sobrenome} - Idade: {x.idade}')

  print('O loop entrou no else')
