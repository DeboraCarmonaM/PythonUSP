quantidade = int(input("Digite quantos números tem a sequência: "))
i = 0
soma = 0



while i != quantidade:
    valor = int(input("Digite um valor a ser somado: "))
    i = i + 1
    soma = soma + valor

print("A soma dos valores digitados é: ", soma)
