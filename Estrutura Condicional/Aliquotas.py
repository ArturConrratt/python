salario = float(input("Digite seu salario"))
if salario <= 20000:
    print ("Voce nao possui aliquotas de imposto de renda")
elif 20001 <= salario <= 50000:
    aliquota1 = salario * 0.15
    print ("Sua aliquota é:", aliquota1)
else:
    aliquota2 = salario * 0.25
    print ("Sua aliquota é:", aliquota2)
