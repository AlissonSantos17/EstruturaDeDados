import carro, moto, veiculo, pessoa

punto_branco = carro.Carro('Branco', 'flex', 1.0, 4)
punto_branco.ligar()
punto_branco.abastecer(50)
punto_branco.abastecer(10)
punto_branco.acelerar(20)
punto_branco.pintar('Preto')
print(punto_branco.cor)
print(f'A quantidade de combustível do Punto Branco é: L\n')

moto_vermelha = moto.Moto('Vermelha', 'Gasolina', 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)

