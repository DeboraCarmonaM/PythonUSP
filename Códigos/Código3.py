contador = 1
gasto = 0
while contador <= 8:
    lanche = float(input('Quanto você gastou com o lanche hoje? '))
    gasto = gasto + lanche
    contador = contador + 1
print('O total de gastos foi R${}'.format(gasto)) 
