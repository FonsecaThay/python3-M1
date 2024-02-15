from math import hypot
a=float(input("Digite o cateto oposto:"))
b=float(input("Digite o cateto adjacente:"))

hi= hypot(a, b)

print('A hipotenusa vai medir {:.2f}'.format(hi))