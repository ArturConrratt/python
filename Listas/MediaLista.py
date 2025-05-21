quantidade_alunos = int(input("Informe a quantidade de alunos: "))

notas = []

for i in range(quantidade_alunos):
    while True:
        try:
            nota = int(input(f"Digite a nota do aluno {i + 1} (0 a 100): "))
            if 0 <= nota <= 100:
                notas.append(nota)
                break
            else:
                print("Nota inválida. A nota deve ser entre 0 e 100.")
        except ValueError:
            print("Por favor, digite um número inteiro válido para a nota.")

abaixo_da_media = 0
na_media = 0

for nota in notas:
    if nota < 60:
        abaixo_da_media += 1
    elif nota == 60:
        na_media += 1

print(f"\nTotal de alunos abaixo da média: {abaixo_da_media}")
print(f"Total de alunos na média (nota 60): {na_media}")