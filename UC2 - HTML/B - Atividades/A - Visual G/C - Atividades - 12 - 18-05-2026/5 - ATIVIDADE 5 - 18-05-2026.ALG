Algoritmo "Atividade 5 - 18-05-2026"

Var
salario_novo, salario_antigo: real

Inicio

escreval ("Qual seu salário? (em R$)")
leia (salario_antigo)



se (salario_antigo <= 1500) entao
salario_novo <- salario_antigo * 1.15
    escreval("Você receberá aumento de 15% e seu salário novo será de R$", salario_novo)
senao
    se (salario_antigo <= 3000) entao
salario_novo <- salario_antigo * 1.10
    escreval("Você receberá aumento de 10% e seu salário novo será de R$", salario_novo)
senao
    salario_novo <- salario_antigo * 1.05
    escreval("Você receberá aumento de 5% e seu salário novo será de R$", salario_novo)
fimse
    fimse
Fimalgoritmo