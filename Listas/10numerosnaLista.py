a = []

for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            a.append(numero)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

print("\nLista com os números digitados:",a )