d = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos Km rodados?'))
pg = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R${pg:.2f}')
