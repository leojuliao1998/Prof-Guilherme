print("===== Escolha o gênero para recomendação de filme =====")
print("A - Ação")
print("b - Terror")
print("C - Comédia")
print("D - Ficção Científica")
print("=======================================================")

filme = input("Selecione a letra correspondente: ").upper()

# ou então coloco .lower() para as letras serem minúsculas.

match filme:
    case "A" | "a":
        print("O filme recomendado para o gênero de Ação é Veloses e Furioso")
    
    case "B" | "b":
        print("O filme recomendado para o gênero de Terror é Pânico")

    case "C":
        print("O filme recomendado para o gênero de Comédia é Uma Comédia Nada Romântica")
    
    case "D":
        print("O filme recomendado para o gênero de Ficção Científica é De Volta para o Futuro")

    case _:
        print("Opção inválida, selecione uma opção da lista")