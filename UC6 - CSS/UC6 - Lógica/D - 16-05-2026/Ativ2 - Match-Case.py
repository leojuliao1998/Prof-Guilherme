print("<=== Verifique o status do seu pedido ===>")
print("Novo")
print("Pendente")
print("Pago")
print("Enviado")
print("Entregue")
print(" ")

# Não é necessário colocar essa parte de cima, fica só como estética.
# Posso deixar apenas a parte de baixo, a variável, o match e os cases.
pedido = input("Digite o status do seu pedido: ").lower()
match pedido: # <-Posso colocar aqui também .lower()
    case "novo":
        print("Pedido criado.")
    case "pendente":
        print("Seu pedido está aguardando pagamento.")
    case "pago":
        print("Pagamento confirmado! Preparando envio.")
    case "enviado":
        print("Seu pedido está a caminho.")
    case "entregue":
        print("Pedido finalizado.")
    case _:
        print("Status desconhecido.")
print(" ")