print("Saiba a classificação das idades")

idade = int(input("Idade: "))

if idade < 13:
    print("Criança")

elif idade < 18:
    print("Adolescente")

elif idade < 60:
    print("Adulto")
    
else:
    print("Idoso")