import math
an = float(input("Digite o angulo que vc deseja saber:"))

seno = math.sin(math.radians(an))
cs = math.cos(math.radians(an))
tg = math.tan(math.radians(an))

print("O seno do angulo {} é:{:.2f}".format(an, seno))
print("O cosseno do angulo {} é:{:.2f}".format(an, cs))
print("A tangente do angulo {} é:{:.2f}".format(an, tg))