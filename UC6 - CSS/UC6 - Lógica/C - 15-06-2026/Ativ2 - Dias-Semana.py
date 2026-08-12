print("===== Menu semanal =====")
print("1 - Segunda-Feira")
print("2 - Terça-Feira")
print("3 - Quarta-Feira")
print("4 - Quinta-Feira")
print("5 - Sexta-Feira")
print("6 - Sábado")
print("7 - Domingo")
print("========================")

dia_semana = int(input("Escolha o dia da semana: "))

match dia_semana:
    case 1:
        print("Segunda-Feira")

    case 2:
        print("Terça-Feira")
    
    case 3:
        print("Quarta-Feira")

    case 4:
        print("Quinta-Feira")

    case 5:
        print("Sexta-Feira")

    case 6:
        print("Sábado")

    case 7:
        print("Domingo")

    case _:
        print("Número inválido")