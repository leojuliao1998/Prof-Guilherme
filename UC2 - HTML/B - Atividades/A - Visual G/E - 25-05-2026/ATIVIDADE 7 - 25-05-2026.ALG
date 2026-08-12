Algoritmo "Atividade 7 - 25-05-2026"

Var
ping: inteiro


Inicio
escreval ("Verifique o PING para rodar o jogo fluidamente!")

escreval ("1 - Ping abaixo de 30 ms é Excelente!")
escreval ("2 - Ping de 30 a 100 ms é rezoável!")
escreval ("3 - Ping acima de 100 ms é LagAlto!")

leia (ping)
escolha (ping)

    caso 1
        escreval ("Seu jogo roda normal!")
    caso 2
        escreval ("Seu jogo pode ter alguns delays, mas ainda é jogável!")
    caso 3
        escreval ("Seu jogo terá muitos delays, será difícil jogar!")
fimescolha




Fimalgoritmo