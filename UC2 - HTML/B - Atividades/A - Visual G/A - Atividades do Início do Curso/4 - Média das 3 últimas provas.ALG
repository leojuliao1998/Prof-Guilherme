Algoritmo "Média das 3 últimas provas"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/04/2026
Var
// Seção de Declarações das variáveis 
Nota_prova1: real
Nota_prova2: real
Nota_prova3: real
Media_das_provas: real

Inicio

escreva ("Nota da primeira prova? ")
leia(nota_prova1)

escreva ("Nota da segunda prova? ")
leia(nota_prova2)

escreva ("Nota da terceira prova? ")
leia(nota_prova3)

Media_das_provas <- (nota_prova1 + nota_prova2 + nota_prova3) / 3

escreva("Sua média das 3 últimas provas é: ", Media_das_provas:1:2)

Fimalgoritmo