'''import math
num = float(input('Digite um valor:'))
print("o valor digitado {} tem a parte inteira {}", format(num, math.trunc(num)))'''

valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor} e a sua porção inteira é {valor.__trunc__()}')