faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o faturamento total
faturamento_total = sum(faturamento.values())

# Calcular o percentual de representação de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: R$ {valor:.2f}".replace(".", ",") + f" ({percentual:.2f}%)")

