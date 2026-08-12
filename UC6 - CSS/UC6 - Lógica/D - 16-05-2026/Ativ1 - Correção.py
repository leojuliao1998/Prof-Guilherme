idade = int(input("Digite sua idade: "))
valor_compra = float(input("Digite o valor da compra: "))

if idade < 12:
    categoria = "Criança"

elif idade < 18:
    categoria = "Adolescente"

elif idade < 59:
    categoria = "Adulto"

else:
    categoria = "Idoso"

# ----------------------------- # 

if valor_compra > 500:
    desconto_parcial = 20

elif valor_compra > 200:
    desconto_parcial = 10

elif valor_compra > 100:
    desconto_parcial = 5

else:
    desconto_parcial = 0

# ----------------------------- #

valor_desconto = valor_compra * (desconto_parcial / 100)
valor_final = valor_compra - valor_desconto

# ----------------------------- #

print("<===== RESULTADO ======>")
print("Categoria do cliente:",categoria)
print("Desconto aplicado:",desconto_parcial,"%")
print(f"Valor original: R${valor_compra:.2f}")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Valor final: R${valor_final:.2f}")