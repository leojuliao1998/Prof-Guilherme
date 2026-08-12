Algoritmo "Atividade 4 - 25-05-2026"

Var
saldo: inteiro
faltante: inteiro


Inicio
escreval ("Evolução de armadura 500 moedas de ouro")
escreval ("Saldo: ")
leia (saldo)

se saldo >= 500 entao
    escreval ("Compra efetivada!")
    senao
    faltante <- 500 - saldo
    escreval ("Compra não realizada! Falta", faltante," moedas de ouro para a compra!")
fimse

Fimalgoritmo