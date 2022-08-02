v = float(input('Coloque seu saldo aqui e descubra quantos dólares você pode comprar: R$'))
uss = v / 5.15
#uss2= v / 3.27
euro = v / 5.82
print(f'Com R${v:.2f} você pode comprar US${uss:.2f} dólares')
print(f'Com R${v:.2f} você pode comprar US${euro:.2f} euros')