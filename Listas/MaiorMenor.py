a = []

for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            a.append(numero)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

maior_numero = max(a)
menor_numero = min(a)

print("\nLista dos números digitados:", a)
print(f"O maior número digitado é: {maior_numero}")
print(f"O menor número digitado é: {menor_numero}")