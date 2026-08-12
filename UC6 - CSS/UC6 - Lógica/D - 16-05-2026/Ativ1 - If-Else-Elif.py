print("======== Bem-vindo a loja Menos é Mais!!! ========")
print("========= Aqui você sempre bem vestida!!! ========")
print(" ")
print("==== Hoje estamos com uma promoção imperdível ====")
print(" ")
print("Nas compras acima de R$ 500 ganha 20% de desconto")
print("Nas compras acima de R$ 200 ganha 10% de desconto")
print("Nas compras de R$ 100 a R$200 ganha 5% de desconto")
print("==================================================")

compra = float(input("Digite o valor da sua compra para cálculo do desconto e valor final: "))
idade = int(input("Digite sua idade: "))

if compra > 500:
    valor_compra = compra - (compra * 0.20)

elif compra > 200:
    valor_compra = compra - (compra * 0.10)

elif compra > 100:
    valor_compra = compra - (compra * 0.05)

else:
    valor_compra = compra

if idade >= 60:
    print(f"Sua classificação de idade é IDOSO e sua compra ficou R$ {valor_compra:.2f}")

elif idade >= 18:
    print(f"Sua classificação de idade é ADULTO e sua compra ficou R$ {valor_compra:.2f}")

elif idade >= 12:
    print(f"Sua classificação de idade é ADOLESCENTE e sua compra ficou R$ {valor_compra:.2f}")

else:
    print(f"Sua classificação de cliente é CRIANÇA e sua compra ficou R$ {valor_compra:.2f}")



