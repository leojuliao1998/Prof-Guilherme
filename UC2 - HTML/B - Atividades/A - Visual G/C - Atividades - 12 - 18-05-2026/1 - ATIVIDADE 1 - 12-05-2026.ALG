Algoritmo "Atividade 1 - 12-05-2026"

Var
veloc_perm, veloc_atual, porcentagem: real

Inicio
escreval ("Digite sau velocidade e a da via para verificação de multa!")
escreval ("Velocidade via(km/h): ")
leia (veloc_perm)

escreval ("Velocidade do carro(km/h): ")
leia (veloc_atual)

porcentagem <- veloc_perm * 1.20

se (veloc_atual <= veloc_perm) entao
   escreval ("Você está ISENTO de multa!")
senao
   se (veloc_atual <= porcentagem) entao
      escreval ("Você cometeu infração MÉDIA, pagará R$130,16")
   senao
      escreval ("Você cometeu infração GRAVÍSSIMA, pagará R$880,41 e CNH suspensa")
   fimse
fimse


Fimalgoritmo