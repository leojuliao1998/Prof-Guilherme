Algoritmo "Preço do combustível"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/04/2026


Var

valor_do_litro: real
tanque_em_mL: real
valor_a_colocar: real


Inicio
// Um motorista deseja colocar no seu tanque R$ 200 de gasolina.
// Escreva um algoritmo para ler o preço do litro da gasolina (R$ 6,96) e o
//valor do pagamento e exibir quantos litros ele conseguiu colocar no tanque.

escreva ("Valor do preço do combustível: ")
leia(valor_do_litro)

escreva ("Valor a ser colocado: ")
leia(valor_a_colocar)

tanque_em_mL <- valor_a_colocar / valor_do_litro

escreva ("A capacidade do tanque de combustível em mL é de: ", tanque_em_mL:1:2)


Fimalgoritmo