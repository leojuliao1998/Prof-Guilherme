numero = int(input("Escolha um número de 1 a 10 para aparecer na tela: "))

match numero:
    case 1:
        print("Número escolhido foi o 1!")

    case 2:
        print("O número escolhido foi o 2!")
    
    case 3:
        print("O número escolhido foi o 3!")

    case 4:
        print("O número escolhido foi o 4!")

    case 5:
        print("O número escolhido foi o 5!")

    case 6:
        print("O número escolhido foi o 6!")

    case 7:
        print("O número escolhido foi o 7!")

    case 8:
        print("O número escolhido foi o 8!")

    case 9:
        print("O número escolhido foi o 9!")

    case 10:
        print("O número escolhido foi o 10!")

    case _:
        print("Número inválido, escreva outro!")