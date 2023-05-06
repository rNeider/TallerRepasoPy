import random


codigo = ""
for i in range(6):
    codigo += str(random.randint(0, 9))

print(codigo)