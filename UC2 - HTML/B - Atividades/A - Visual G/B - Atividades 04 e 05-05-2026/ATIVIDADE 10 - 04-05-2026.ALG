Algoritmo "Atividade 10 - 04-05-2026"

Var
idade: inteiro
obrigada: logico


Inicio

escreval ("A obridatoriedade para votação é de entre 18 a 70 anos de idade.")

escreval ("Digite sua idade para verificação: ")
leia (idade)

obrigada <- (idade >= 18) e (idade <= 70)

escreval ("Você é obrigado(a) a votar?", obrigada)


Fimalgoritmo