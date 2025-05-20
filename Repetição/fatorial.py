n1 = int(input("Digite um número inteiro positivo: "))
if n1 < 0:
    print("Digite um número positivo.")
else:
    f = 1
for i in range(1, n1 + 1):
    f *= i
print(f"O fatorial de {n1} é: {f}")