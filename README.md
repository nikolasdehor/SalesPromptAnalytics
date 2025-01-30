# 🚀 Sales Insights Engine | Meganium Sales Analytics

![Badge](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Badge](https://img.shields.io/badge/Pandas-2.0%2B-orange?logo=pandas)
![Badge](https://img.shields.io/badge/Status-Concluído-brightgreen)

**Transformando dados brutos em estratégias de vendas globais**  
*Um projeto da [DIO](https://www.dio.me/) para análise de dados usando prompts eficientes*

---

## 🌍 Visão Geral
Sistema de análise de vendas para a Meganium - fabricante de consoles portáteis retro (*RG35XX, RG40XXV, CubeXX*). Centraliza e processa dados de 3 marketplaces globais:
- **AliExpress** (Europa/Ásia)
- **Etsy** (América do Norte/Europa)
- **Shopee** (América do Sul/Ásia)

---

## 🔍 Funcionalidades Principais
| Recursos                 | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| **Consolidação de Dados** | Unificação de bases de terceiros em formato padronizado                   |
| **Análise Geográfica**    | Mapeamento de produtos populares por país                                 |
| **Otimização Logística** | Identificação de padrões de transporte e custos                          |
| **KPI Estratégicos**      | Cálculo de ticket médio, eficácia de descontos e tendências sazonais      |

---

## 🎯 Objetivos Alcançados
- [x] `📊 Consolidar bases` de 3 plataformas em estrutura única
- [x] `🌎 Identificar mercados-chave` por país/região
- [x] `📦 Otimizar logística` com base em padrões de entrega
- [x] `🤑 Maximizar receitas` através de análise de produtos premium

---

## 🧩 Estrutura do Projeto
```bash
## 🧩 Estrutura do Projeto
```bash
📂 SalesPromptAnalytics/
├── 📂 scripts              # Dados brutos das plataformas
      ├── 📄 primeiro.py # Carregamento e inspeção inicial dos dados
      ├── 📄 segundo.py  # Análise agregada (receitas, descontos)
      ├── 📄 terceiro.py # Identificação de produtos mais vendidos
      ├── 📄 quarto.py   # Popularidade por país
      ├── 📄 quinto.py   # Tendência mensal de vendas
      ├── 📄 sexto.py    # Cálculo do ticket médio
      ├── 📄 setimo.py   # Análise de eficácia de descontos
      ├── 📄 oitavo.py   # Ranking de países por receita
├── 📂 data              # Dados brutos das plataformas
└── 📄 chatgpt_prompts.md # Diálogo completo com insights gerados

🛠️ Começando
Pré-requisitos
Python 3.10+

Pandas 2.0+

Jupyter Notebook (opcional)

Instalação
bash
Copy
git clone https://github.com/seu-usuario/Meganium-Sales-Analytics.git
pip install pandas numpy
🔑 Principais Insights
python
Copy
# Trecho de análise geográfica (quarto.py)
print(popular_products.query("Country == 'Brasil'"))
Platform	Country	Most Popular Product	Total Quantity
Shopee	Brasil	NEW MEGANIUM RG CubeXX	12
📈 Próximos Passos
Implementar dashboard interativo com Streamlit

Adicionar análise de custo-benefício por rota de entrega

Integrar API de conversão de moedas em tempo real

🤝 Como Contribuir
Faça um fork do projeto

Crie sua branch: git checkout -b feature/nova-analise

Commit suas mudanças: git commit -m 'Add new feature'

Push para a branch: git push origin feature/nova-analise

Abra um Pull Request

📄 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.

Meganium Console