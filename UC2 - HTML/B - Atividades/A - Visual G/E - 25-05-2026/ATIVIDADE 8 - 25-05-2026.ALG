Algoritmo "Atividade 8 - 25-05-2026"


Var
hora_recarga: inteiro
kwh: inteiro
consumo: real


Inicio
escreval ("Recarga entre às 18h e 21h o kWh é R$ 2,50.")
escreval ("Recarga demais horários o kWh é R$ 1,80.")
escreval ("Horário de recarga: ")
leia (hora_recarga)
escreval ("kWh consumido: ")
leia (kwh)

se (hora_recarga >= 18) e (hora_recarga <= 21) entao
consumo <- 2.50 * kwh
    escreval ("Você gastou R$", consumo, " na recarga!")
    senao
consumo <- 1.80 * kwh
    escreval ("Você gastou R$", consumo, " na recarga!")
fimse


Fimalgoritmo