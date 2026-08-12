Algoritmo "Atividade 5 - 25-05-2026"

Var
seguidores: inteiro
faltante: inteiro


Inicio
escreval ("Digite a quantidade de seguires e verifique a afiliação!")
escreval ("Seguidores: ")
leia (seguidores)

se seguidores >= 50 entao
    escreval ("Parabéns, agora você é um afiliado!")
    senao
    
faltante <- 50 - seguidores
    escreval ("Você não alcançou a meta e falta", faltante, " seguidores!")
fimse

Fimalgoritmo