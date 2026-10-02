# PASSO A PASSO
# 1: Titulo - Sistema de Vendas

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
st.write("## Cadastrar Vendas")
data = st.datetime_input("Data")
vendedor = st.selectbox("Vendedor", vendedores)
produto = st.selectbox("Produto", produtos)
quantidade = st.number_input("Quantidade", step=1)
valor = st.number_input("Valor")
botao_cadastrar = st.button("Cadastrar Venda")

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
grafico2 = px.pie(tabela_vendas, names = "produtos", values= "valor")
st.plotly_chart(grafico2)