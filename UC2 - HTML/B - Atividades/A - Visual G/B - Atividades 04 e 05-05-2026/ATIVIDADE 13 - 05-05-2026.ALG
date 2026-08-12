Algoritmo "Atividade 13 - 05-05-2026"



Var
peso: real
altura: real
imc: real



Inicio
escreval ("Digite seu peso e altura, descubra seu IMC e veja se está acima ou abaixo do peso!")
escreva ("Peso(em kg): ")
leia (peso)

escreva ("Altura(em mts): ")
leia (altura)

imc <- peso / (altura * altura)

escreval ("Seu IMC é de ", imc:1:1)

se (imc <= 18.4) entao
escreval ("Você está com magreza extrema")
senao

se (imc >= 18.5) e (imc <= 24.9) entao
escreval ("Você está com o peso normal")
senao

se (imc >= 25) e (imc <= 29)  entao
escreval ("Você está com sobrepeso")
senao

se (imc >= 30) e (imc <= 34.9) entao
escreval ("Você está com o obesidade grau I")
senao

se (imc >= 35) e (imc <= 39.9) entao
escreval ("Você está com o obesidade grau II")

senao
escreval ("Você está com o obesidade grau III")
fimse
fimse
fimse
fimse
fimse

Fimalgoritmo