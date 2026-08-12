Algoritmo "Atividade 15 - 05-05-2026"

Var
login: caractere
senha: inteiro
autorizado: logico


Inicio

escreval ("Digite login e senha para acesso ao sistema Senac!")

escreva ("Login: ")
leia (login)

escreva ("Senha: ")
leia (senha)

se (autorizado = "leonardo") e (senha = "123456") entao
escreval ("Acesso permitido, entrando!")

senao
escreval ("Usuário ou senha incorretos!")
fimse

Fimalgoritmo