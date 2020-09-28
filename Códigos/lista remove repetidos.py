def remove_repetidos(x):

    lista = x
    i = 0
    while i < len(lista):
        y = i + 1
        while y < len(lista):
            if lista[y] == lista[i]:
                del(lista[y])
            else:
                y = y + 1
        i = i + 1

    return sorted(lista)
