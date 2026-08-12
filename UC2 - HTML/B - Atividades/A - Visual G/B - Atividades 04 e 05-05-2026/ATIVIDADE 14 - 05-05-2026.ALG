Algoritmo "Atividade 14 - 05-05-2026"



Var
nota1, nota2, nota3, nota4, media: real



Inicio
escreval ("Digite suas notas e verifique sua aprovação.")
escreva ("Nota 1: ")
leia (nota1)

escreva ("Nota 2: ")
leia (nota2)

escreva ("Nota 3: ")
leia (nota3)

escreva ("Nota 4: ")
leia (nota4)

media <- (nota1 + nota2 + nota3 + nota4) / 4


escreval ("Sua média é de: ", media:1:1)


se (media > 7) entao
escreval ("Você está aprovado!")
fimse

se (media > 5 ) e (media < 6.9) entao
escreval ("Você está de recuperação!")
fimse

se (media < 4.9) entao
escreval ("Você está reprovado!")
fimse



Fimalgoritmo