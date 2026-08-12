Algoritmo "Atividade 10 - 25-05-2026"

Var
mhs: inteiro
kwh: real


Inicio
escreval ("Na mineração de criptomoeda é necessário ter MH/s e kWs específicos")

escreval ("Digite sua taxa MH/s: ")
leia (mhs)

escreval ("Digite o valor de kWh da sua cidade: ")
leia (kwh)

se (mhs >= 50) e (kwh <= 0.40) entao
    escreval ("A mineração é viável!")
    senao
    escreval ("Infelizmente não tem viabilidade para minerar!")
fimse


Fimalgoritmo