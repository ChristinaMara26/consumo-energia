
#Projeto app.py - Agenda 05
#Consumo de energia
#Autora: Christina Mara Tessari

# --- ENTRADA ---
nome_aparelho=input("Digite o nome do aparelho:")
potencia_aparelho=float(input("Digite a potência do aparelho em Watts(W):"))
tempo_medio_diario_horas=float(input("Digite o tempo médio diário horas de uso do aparelho:"))

# --- PROCESSAMENTO ---
consumo_mensal_KWh=(potencia_aparelho*tempo_medio_diario_horas*30)/1000
custo_estimado=consumo_mensal_KWh*0.75

# --- SAÍDA ---
print(f"aparelho {nome_aparelho}")
print(f"Consumo estimado:{consumo_mensal_KWh:.2f} KWh/mes")
print(f"Custo estimado R${custo_estimado:.2f} Reais")


