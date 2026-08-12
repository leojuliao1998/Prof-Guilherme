Algoritmo "Atividade 7 (Gemini) - 18-05-2026"

var
   dia, mes, ano: inteiro
   ultimoDia: inteiro
   bissexto: logico

inicio
   // 1. Entrada de dados
   escreva("Digite o dia (DD): ")
   leia(dia)
   escreva("Digite o mês (MM): ")
   leia(mes)
   escreva("Digite o ano (AAAA): ")
   leia(ano)

   // 2. Verificar se o ano é bissexto
   // Regra: divisível por 4 e não por 100, ou divisível por 400
   bissexto <- (ano % 4 = 0) e (ano % 100 <> 0) ou (ano % 400 = 0)

   // 3. Definir quantos dias o mês atual possui
   escolha mes
      caso 1, 3, 5, 7, 8, 10, 12
         ultimoDia <- 31
      caso 4, 6, 9, 11
         ultimoDia <- 30
      caso 2
         se (bissexto) entao
            ultimoDia <- 29
         senao
            ultimoDia <- 28
         fimse
   fimescolha

   // 4. Lógica para incrementar a data
   dia <- dia + 1

   se (dia > ultimoDia) entao
      dia <- 1
      mes <- mes + 1

      se (mes > 12) entao
         mes <- 1
         ano <- ano + 1
      fimse
   fimse

   // 5. Resultado
   escreval("O dia seguinte é: ",dia," /",mes," /",ano)

fimalgoritmo