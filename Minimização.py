import pulp

# Definir o problema
modelo = pulp.LpProblem("Problema_Minimizacao", pulp.LpMinimize)

# Variáveis de decisão
x1 = pulp.LpVariable('Projeto_moveis', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('Projetos_Web', lowBound=0, cat='Integer')

# Função objetivo
modelo += 30 * (10 * x1 + 6 * x2) + 50 * (5 * x1 + 10 * x2), "Custo_Total"

# Restrições
modelo += x1 >= 3
modelo += x2 >= 2

# Resolver
modelo.solve()

# Exibir resultados
print("Status:", pulp.LpStatus[modelo.status])
print("Projetos Moveis (x1):", x1.varValue)
print("Projetos Web (x2):", x2.varValue)
print("Custo Total:", pulp.value(modelo.objective))
