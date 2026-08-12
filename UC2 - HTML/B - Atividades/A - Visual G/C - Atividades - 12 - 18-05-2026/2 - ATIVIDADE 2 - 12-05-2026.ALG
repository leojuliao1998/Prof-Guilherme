Algoritmo "Atividade 2 - 12-05-2026"

Var
lado_a, lado_b, lado_c:real


Inicio
escreval ("Digite os tamanhos dos lados do descubra qual tipo de triângulo!")
escreva ("Lado A: ")
leia (lado_a)

escreva ("Lado B: ")
leia (lado_b)

escreva ("Lado C: ")
leia (lado_c)

//Verificação da existência (Regra: cada lado < soma dos outros dois)
se (lado_a < lado_b + lado_c) e (lado_b < lado_a + lado_c) e (lado_c < lado_a + lado_b) entao

// 2. Verificação do tipo
   se (lado_a = lado_b) e (lado_b = lado_c) entao
      escreval("Triângulo Equilátero")
   senao
      se (lado_a = lado_b) ou (lado_a = lado_c) ou (lado_b = lado_c) entao
         escreval("Triângulo Isósceles")
      senao
         escreval("Triângulo Escaleno")
fimse
fimse
senao
escreval ("Não forma triângulo")
fimse


Fimalgoritmo