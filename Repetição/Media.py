n1 = input("Digite numeros para que a media seja feita, separe eles por espaços:")
numeros = [float(num) for num in n1.split()]
soma = 0
for numero in numeros:
    soma += numero
    media = soma / len(numeros)
print(f"A média dos números dados: {media}")
