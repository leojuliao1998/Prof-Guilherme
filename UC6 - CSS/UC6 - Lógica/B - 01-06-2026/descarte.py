print("Selecione qual tipo de lixo e descubra a quantidade de tempo em média, que leva de decomposição dos materiais")
print("Plastico / Papel / Vidro / Metal / Orgânico")

#todo .lower() - Tudo que a pessoa escrever, ser recebido pelo sistema como letra minúscula #
#todo .strip() - Se a pessoa digitar algum espaço sem querer, o sistema já receber sem o espaço #

material = input("Material: ").lower().strip()

if material == "plastico" or material == "plástico":
    print("Lixeira VERMELHA🔴! Tempo de decomposição: ~ 450 anos.")
elif material == "papel":
    print("Lixeira AZUL🔵! Tempo de decomposição: 3 a 6 meses.")
elif material == "vidro":
    print("Lixeira VERDE🟢! Tempo de decomposição: Indeterminado (~ milhares de anos)")
elif material == "metal":
    print("Lixeira AMARELA🟡! Tempo de decomposição: Mais de 100 anos.")
elif material == "organico" or material == "orgânico":
    print("Lixeira MARROM🟤! Pode ser usado para compostagem! (Virar adubo!)")
else:
    print("Opção inválida❌! Por favor, escolha um material cadastrado.")