Algoritmo "Atividade 9 - 04-05-2026"

Var
prova1, prova2, frequencia, media: real
aprovacao: logico

Inicio

escreval ("Digite a nota da sua prova 1: ")
leia (prova1)

escreval ("Digite a nota da sua prova 2: ")
leia (prova2)

escreval ("Digite a frequencia do aluno: ")
leia (frequencia)

media <- (prova1 + prova2) / 2

aprovacao <- (media >= 7) e (frequencia > 75)

escreval ("Aprovado?", aprovacao)



Fimalgoritmo