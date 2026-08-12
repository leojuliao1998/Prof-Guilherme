print("Descubra seu IMC!")
print("--------------------------------------------")
peso = float(input("Digite seu peso(em kg): "))
altura = float(input("Digite sua altura(em m): "))

alt_alt = altura * altura
imc = peso / alt_alt
print("--------------------------------------------")
print("Seu IMC é", imc)

if imc < 18.5:
    print("Você está ABAIXO DO PESO! Procure um Nutricionista!")

elif imc < 25:
    print("Você está com PESO NORMAL!")

elif imc < 30:
    print("Você está com SOBREPESO! Procure um Nutricionista!")

elif imc < 40:
    print("Você está com OBESIDADE! Procure um Nutricionista!")

else:
    print("Você está com OBESIDADE GRAVE! Procure um Nutricionista!")

print("--------------------------------------------")