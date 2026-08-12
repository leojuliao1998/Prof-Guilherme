banho = int(input("Tempo médio do banho diariamente (min): "))
print("")
maquina_lavar = int(input("Quantidade de vezes por semana a máquina de lavar é ligada: "))
print("")
mangueira = int(input("Quantos minutos a mangueira fica ligada semanalmente para lavar a calçada ou lavar o carro (min): "))

#^ gasto banho #
gasto_diario_banho = banho * 9
gasto_mensal_banho = gasto_diario_banho * 30

#^ gasto maquina de lavar #
gasto_semanal_maquina = maquina_lavar * 1200
gasto_mensal_maquina = gasto_semanal_maquina * 4

#^ gasto mangueira #
gasto_semanal_mangueira = mangueira * 10
gasto_mensal_mangueira = gasto_semanal_mangueira * 4

print("")

print("Você gasta no banho diariamente",gasto_diario_banho,"L de água e o gasto mensalmente é de",gasto_mensal_banho,"L de água!")
print("")
print("Já na maquina de lavar, semanlmente",gasto_semanal_maquina,"L de água e mensalmente o gasto é de",gasto_mensal_maquina,"L de água!")
print("")
print("Na mangueira o gasto é de",gasto_semanal_mangueira,"L de água semanal e mensal é de",gasto_mensal_mangueira,"L de água!")
print("")