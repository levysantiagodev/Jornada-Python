# PASSO A PASSO
# Titulo - Sistema de Vendas

# Seção cadastrar vendas
    # Campo de data
    # Campo Vendedor
    # Campo Produto
    # Campo Qtd
    # Campo Valor
    # Botão cadstrar vendas

# Seção Vendas Cadastradas
    # Tabela de vendas

# Dashboard
    # Card/Métrica - Faturamento total
    # Gráfico de barra/coluna - venda por vendedor
    # Gráfico de pizza - venda por produto

# FERRAMENTAS USADAS
# streamlit
# pandas
# plotly

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

# Variáveis
vendedores = ["Ana", "Bruno", "Carla"]
produtos = ["Notebook", "Celular", "Fone"]

# TÍTULO
st.write("# SISTEMA DE VENDAS")

# SEÇÃO DE CADASTRO DE VENDAS
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", vendedores)
produto = st.sidebar.selectbox("Produto", produtos)
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Lógica do botão de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # Encontra a última linha no banco de dados
    tabela_vendas.loc[ultima_linha] = nova_venda # Adiciona a nova venda na última linha
    tabela_vendas.to_csv("vendas.csv", index = False) # Atualizando o banco de dados
    st.success("Venda Cadastrada")

# SEÇÃO DE VISUALIZAR VENDAS
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# SEÇÃO DE DASHBOARDS
st.write("## Dashboard")

# Card/Métrica - Faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico de barra/coluna - venda por vendedor
grafico1 = px.bar(tabela_vendas, x = "vendedor", y = "valor", color = "produto")
st.plotly_chart(grafico1)

# Gráfico de pizza - venda por produto
grafico2 = px.pie(tabela_vendas, names = "produto", values= "valor", hole = 0.5)
st.plotly_chart(grafico2)