import pulp


dados = {
    'Search': {'custo_slot': 200,'conv_per_slot': 8, 'revenue_per_conv':45,
               'max_slots': 10,'min_slots':1},
    'Social': { 'custo_slot':120,'conv_per_slot':4,'revenue_per_conv':30,
               'max_slots':12,'min_slots':0},
    'Display': {'custo_slot':80,'conv_per_slot':1.5,'revenue_per_conv':25,
                'max_slots':20,'min_slots': 0}    
}

# Orçamento total disponível para compra de slots (R$)
orcamento_total = 2500

modelo= pulp.LpProblem("MAximizar_lucros_Ads",pulp.LpMaximize)

# Variáveis de decisão: número de slots (inteiros)
slots = {c: pulp.LpVariable(f"slot_{c}",lowBound=0,cat='Integer')
         for c in dados}

modelo += pulp.lpSum(
       ((dados[c]['conv_per_slot'] * dados[c]['revenue_per_conv']) - dados[c]['custo_slot']) * slots[c]
   for c in dados
), "Lucro_Esperado_Total"

# 1) Orçamento: soma(custo_slot * slots) <= orcamento_total
modelo += pulp.lpSum(dados[c]['custo_slot'] * slots[c] for c in dados) <= orcamento_total, "Restricao_Orcamento"
# 2) Limites máximos por canal
for c in dados:
   modelo += slots[c] <= dados[c]['max_slots'], f"MaxSlots_{c}"
# 3) Mínimos por canal (se aplicável)
for c in dados:
   modelo += slots[c] >= dados[c]['min_slots'], f"MinSlots_{c}"

   modelo.solve(pulp.PULP_CBC_CMD(msg=False))


print("Status:",pulp.LpStatus[modelo.status])
total_receita = sum(
   dados[c]['conv_per_slot'] * dados[c]['revenue_per_conv'] * 
   slots[c].varValue for c in dados)
total_lucro = pulp.value(modelo.objective)

print("\nAlocação de slots por canal:")
for c in dados:
   print(f"  {c}: {slots[c].varValue} slots")
print(f"\nCusto total gasto: R$ {total_custo:.2f}")
print(f"Receita esperada total: R$ {total_receita:.2f}")
print(f"Lucro/valor objetivo (esperado): R$ {total_lucro:.2f}")