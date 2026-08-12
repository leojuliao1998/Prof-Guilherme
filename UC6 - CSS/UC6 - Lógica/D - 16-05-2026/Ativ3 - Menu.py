print("<-=-=-= Menus de opções -=-=-=>")
print ("1")
print ("2")
print ("3")
print ("8")
print ("9")
print ("0")
print ("Sair")
menu = input("Escolha a opção desejada: ")

match menu:
    case "1" | "2" | "3":
        print("Carregando o jogo...")
    case "8" | "9":
        print("Abrindo configurações...")
    case "0" | "Sair":
        print("Saindo do sistema...")
    case _:
        print("Opção não encontrada, selecione uma opção válida!")