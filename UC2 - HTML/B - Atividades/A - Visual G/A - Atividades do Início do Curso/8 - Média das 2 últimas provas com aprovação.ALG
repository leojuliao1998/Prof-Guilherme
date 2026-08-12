Algoritmo "semnome"



Var
Prova_1: real
Prova_2: real
Media_provas: real
Aprovado: logico


Inicio
escreva ("Nota da primeira prova? ")
leia(Prova_1)

escreva ("Nota da segunda prova? ")
leia(Prova_2)

Media_provas <- (Prova_1 + Prova_2) / 2

Aprovado <- Media_provas >= 7

escreva("Sua média das 2 últimas provas é: ", Aprovado)





Fimalgoritmo