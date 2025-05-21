n1 = int(input("Digite um número inteiro: "))
if n1 < 2:
    print(f"O número {n1} não é primo.")
else:
    is_primo = True
    for i in range(2, n1):
        if n1 % i == 0:
            is_primo = False
            break
if is_primo:
    print(f"O número {n1} é primo.")
else:
    print(f"O número {n1} não é primo.")
