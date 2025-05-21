numeros = []

for i in range(5):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

maior_par = None
menor_impar = None
soma = 0

for numero in numeros:
    soma += numero
    if numero % 2 == 0:  
        if maior_par is None or numero > maior_par:
            maior_par = numero
    else:  
        if menor_impar is None or numero < menor_impar:
            menor_impar = numero

media = soma / len(numeros)

print("\nResultados:")
if maior_par is not None:
    print(f"Maior elemento par: {maior_par}")
else:
    print("Não há elementos pares na lista.")

if menor_impar is not None:
    print(f"Menor elemento ímpar: {menor_impar}")
else:
    print("Não há elementos ímpares na lista.")

print(f"Soma dos elementos: {soma}")
print(f"Média dos elementos: {media:.2f}")