n1 = int(input("Digite um numero inteiro:"))
n2 = int(input("Digite outro numero inteiro:"))
i= 0
print(f"\nTabuada de {n1}:")
for i in range(1, 11):
    print(f"{n1} x {i} = {n1 * i}")
    print(f"\nTabuada de {n2}:")
for i in range(1, 11):
    print(f"{n2} x {i} = {n2 * i}")
