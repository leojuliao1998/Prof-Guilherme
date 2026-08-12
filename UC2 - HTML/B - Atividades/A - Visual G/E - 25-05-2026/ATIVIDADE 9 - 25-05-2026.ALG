Algoritmo "Atividade 9 - 25-05-2026"

Var
orcamento: real


Inicio
escreval ("Digite o seu orçamento para ver qual plano assinar!")
leia (orcamento)

se (orcamento < 25) entao
    escreval ("Orçamento abaixo do necessário para assinatura!")
    senao
    se (orcamento >= 25) e (orcamento <= 44.99) entao
    escreval ("Recomendado Plano Padrão!")
    senao
    escreval ("Recomendado Plano Premium 4K!")
fimse
    fimse


Fimalgoritmo