print ('==========TESTE AULA 09==========')
frase = 'Curso em Vídeo Python'
print (frase)
print (frase [3])
print (frase [3:13])
print (frase [:13])
print (frase [13:])
print (frase [1:15])
print (frase [1:15:2])
print (frase [1::2])
print (frase [::2])

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ut volutpat nisl. Duis fermentum lectus a justo congue posuere. Aenean imperdiet imperdiet turpis vitae eleifend. Pellentesque eu nunc sit amet lorem scelerisque aliquam. Proin hendrerit, mauris in hendrerit porta, massa lacus aliquam neque, ornare varius dolor arcu placerat lorem. Aliquam et imperdiet neque. Curabitur et pulvinar felis, in pulvinar ipsum. Mauris tempor commodo ante, id blandit arcu consectetur quis. Curabitur elit lorem, imperdiet eget pretium non, fringilla ut dui.""")

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
frase = frase.replace('Python', 'Android')
print(frase)
print ('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print (dividido[0])
print(dividido[2][3])
print ('--------------------------------------')