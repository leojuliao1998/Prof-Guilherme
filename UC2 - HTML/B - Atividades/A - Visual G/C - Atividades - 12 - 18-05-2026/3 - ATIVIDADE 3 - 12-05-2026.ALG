Algoritmo "Atividade 3 - 12-05-2026"

Var
salario, porcentagem, parcela: real

Inicio

escreval ("Digite seu salário e qual valor de parcela deseja pagar para possibilidade de empréstimo!")
escreva ("Salário bruto(R$): ")
leia (salario)

escreva ("Parcela a ser paga: (R$): ")
leia (parcela)

porcentagem <- salario * 0.30

se (parcela <= porcentagem) entao
   escreval ("Empréstimo concedido!")
senão
   escreval ("Empréstimo negado, a parcela excede o limite de R$ ", porcentagem:5:2)
fimse
Fimalgoritmo
