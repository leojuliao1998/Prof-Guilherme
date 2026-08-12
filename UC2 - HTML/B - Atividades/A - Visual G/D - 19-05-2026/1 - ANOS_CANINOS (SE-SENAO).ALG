Algoritmo "Anos Caninos - 19-05-2026"

Var
idade_humana: inteiro
idade_canina: inteiro


Inicio

escreval ("Descubra a idade humana do seu doguinho!")
escreva ("Digite a idade canina dele: ")
leia (idade_canina)

escreval ("-----------------------------------------------------------")
escreval ("1 ano canino - 15 anos humanos")
escreval ("2 anos caninos - 9 anos humanos")
escreval ("a partir de 3 anos caninos, cada anos conta 5 anos humanos")
escreval ("-----------------------------------------------------------")

limpatela

se idade_canina = 1 entao
    escreval ("Seu doguinho tem 15 anos humanos")
senao
    se idade_canina = 2 entao
        idade_humana <- 15 + 9
    escreval ("Seu doguinho tem", idade_humana, " anos humanos")
senao
    se idade_canina > 2 entao
        idade_humana <- 15 + 9 + (idade_canina - 2) * 5
    escreval ("Seu doguinho tem", idade_humana, " anos humanos")

fimse
fimse
fimse

Fimalgoritmo