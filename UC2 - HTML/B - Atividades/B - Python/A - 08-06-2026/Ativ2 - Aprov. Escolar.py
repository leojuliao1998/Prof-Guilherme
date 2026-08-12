print("Verifique sua aprovação escolar digitando sua nota abaixo")

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Você está APROVADO!")

elif nota >= 5:
    print("Você está em RECUPERAÇÃO!")

else:
    print("Você está REPORVADO!")