Algoritmo "Atividade 6 - 25-05-2026"

Var
senha: inteiro
verificacao: inteiro

Inicio
escreval ("Para entrar no sistema digite a senha de 4 dígitos: ")
leia (senha)
escreval ("Digite o código da verificação de 2 fatores 2FA: ")
leia (verificacao)

se (senha = 1234) e (verificacao = 9988) entao
    escreval ("Acesso concedido!")
    senao
    escreval ("Acesso negado! Tente novamente!")
fimse


Fimalgoritmo