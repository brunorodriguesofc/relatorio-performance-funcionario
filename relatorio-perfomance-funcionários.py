#Relatório de Performance de Funcionários com Bônus

#🔹 REGRAS:

#📊 Bônus
#bônus 1 → R$2 por venda
#bônus 2 → 1% do valor vendido


#📈 Classificação da equipe (pela média de vendas)
#≥ 2000 → Alta performance
#≥ 1000 → Média performance
#< 1000 → Baixa performance


#🔹 DADOS INICIAIS (use exatamente isso)

vendas = {
    "André": [1000, 500, 300],
    "Andressa": [1500, 9000, 300],
    "Alan": [800, 100],
    "Ana": [800, 900, 950]
}


#1. Criar função

def calcular_bonus(lista_vendas):
    bonus1 = len(lista_vendas) * 2
    bonus2 = sum(lista_vendas) * 0.01
    return bonus1, bonus2


#2. Loop principal

total_funcionarios = len(vendas)
total_geral_vendas = 0
total_bonus1 = 0
total_bonus2 = 0
melhor_vendedor = ""
maior_venda = 0
relatorio_funcionarios = ""

for nome, lista in vendas.items():
    total_vendido = sum(lista)
    bonus1, bonus2 = calcular_bonus(lista)  # unpacking da tupla

    total_geral_vendas += total_vendido
    total_bonus1 += bonus1
    total_bonus2 += bonus2

    if total_vendido > maior_venda:
        maior_venda = total_vendido
        melhor_vendedor = nome

    relatorio_funcionarios += f"{nome} → Vendas: R${total_vendido:,.2f} | Bônus1: R${bonus1:,.2f} | Bônus2: R${bonus2:,.2f}\n"


#3. Calcular média geral

media_vendas = total_geral_vendas / total_funcionarios


#4. Classificação

if media_vendas >= 2000:
    classificacao = "Alta performance"
elif media_vendas >= 1000:
    classificacao = "Média performance"
else:
    classificacao = "Baixa performance"


#🔹 SAÍDA FINAL 

print()
print("RELATÓRIO DE PERFORMANCE")
print()
print(f"Total de funcionários: {total_funcionarios}")
print()
print(f"Resumo por funcionário:")
print(relatorio_funcionarios)
print(f"Total geral de vendas: R${total_geral_vendas:,.2f}")
print()
print(f"Total de bônus 1: R${total_bonus1:,.2f}")
print(f"Total de bônus 2: R${total_bonus2:,.2f}")
print()
print(f"Melhor vendedor: {melhor_vendedor}")
print()
print(f"Média de vendas por funcionário: R${media_vendas:,.2f}")
print(f"Classificação da equipe: {classificacao}")
print()
