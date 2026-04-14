# Relatório de Performance de Funcionários com Bônus

## 📌 Descrição
Este projeto simula um sistema de análise de desempenho de funcionários com base em vendas realizadas.

O sistema calcula:
- Total de vendas por funcionário
- Bônus baseado em regras de negócio
- Total geral de vendas
- Média de desempenho da equipe
- Classificação da equipe
- Melhor vendedor

---

## ⚙️ Regras de Negócio

### 📊 Bônus
- Bônus 1: R$2 por venda realizada
- Bônus 2: 1% do valor total vendido

### 📈 Classificação da equipe
- ≥ 2000 → Alta performance
- ≥ 1000 → Média performance
- < 1000 → Baixa performance

---

## 🧠 Funcionalidades

- Cálculo automático de bônus por funcionário
- Identificação do melhor vendedor
- Cálculo de média de vendas da equipe
- Geração de relatório consolidado no terminal

---

## 🛠️ Tecnologias utilizadas

- Python 3

---

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/brunorodriguesofc/relatorio-performance-funcionarios.git

2.	Acesse a pasta:

cd relatorio-performance-funcionarios

3.	Execute o script:

python main.py

⸻

📊 Exemplo de saída

RELATÓRIO DE PERFORMANCE

Total de funcionários: 4

Resumo por funcionário:
André → Vendas: R$1.800,00 | Bônus1: R$6,00 | Bônus2: R$18,00
Andressa → Vendas: R$10.800,00 | Bônus1: R$6,00 | Bônus2: R$108,00
Alan → Vendas: R$900,00 | Bônus1: R$4,00 | Bônus2: R$9,00
Ana → Vendas: R$2.650,00 | Bônus1: R$6,00 | Bônus2: R$26,50

Total geral de vendas: R$16.150,00

Total de bônus 1: R$22,00
Total de bônus 2: R$161,50

Melhor vendedor: Andressa

Média de vendas por funcionário: R$4.037,50
Classificação da equipe: Alta performance

📌 Autor

Bruno Rodrigues
