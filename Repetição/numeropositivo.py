n1 = int(input("Digite um numero inteiro positivo:"))
if n1 > 0:
    soma = 0
    for num in range (1, n1 + 1, 2):
        soma += num
    print(f"A soma dos numeros impares até {n1} é {soma}")
else:
    print("O numero digitado é negativo.")
