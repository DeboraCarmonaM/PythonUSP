import math

x1 = float(input("Digite o x"))
y1 = float(input("Digite o y"))
x2 = float(input("Digite o x"))
y2 = float(input("Digite o y"))

distancia = math.sqrt (((x1-x2)**2) + ((y1 - y2) ** 2))

if distancia >= 10:
    print("longe")

else:
    print("perto")




