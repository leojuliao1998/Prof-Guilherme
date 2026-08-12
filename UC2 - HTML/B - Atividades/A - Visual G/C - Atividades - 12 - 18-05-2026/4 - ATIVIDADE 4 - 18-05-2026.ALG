Algoritmo "Atividade 4 - 18-05-2026"

Var
poluicao: real



Inicio
escreval ("Descubra qual grupo de poluíção sua indústria está!")
leia (poluicao)

se (poluicao <= 0.3) entao
    escreval ("Sua empresa está com índice aceitável de poluíção!")
senao
    se (poluicao > 0.3)  entao
        escreval ("Sua empresa está intimada a suspender as atividades!")
senao
     se (poluicao >= 0.4) entao
        escreval ("Sua empresa deverá suspender temporariamente as atividades!")
senao
     se (poluicao >= 0.5) entao
        escreval ("Sua empresa deverá parar permanentemente as atividades!")
fimse
    fimse
    fimse
    fimse

Fimalgoritmo