cont = 0
soma_medias = 0
while cont < 3:
    nome = str(input("Digite o seu nome:"))
    n1 = float(input("Digite um numero:"))
    n2 = float(input("Digite outro numero:"))
    n3 = float(input("Digite mais um numero:"))
    n4 = float(input("Digite um ultimo numero:"))
    media = (n1 + n2 + n3 + n4) / 4
    soma_medias += media
    print ("Nome:", nome)
    print("Media anual:", media)
    if media >= 7:
        print("aprovado!")
    else:
        print("reprovado!")
        cont += 1
        media_total = soma_medias / cont
print (f"A media total é: {media_total: .2f}")
