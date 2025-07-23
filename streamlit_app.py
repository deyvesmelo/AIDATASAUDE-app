import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI DATA SAÚDE", layout="wide")

st.title("AI DATA SAÚDE 🩺")
st.write("Este app lê arquivos CSV de dados de saúde e gera visualizações e insights rápidos.")

# Upload de arquivo CSV
data_file = st.file_uploader("Faça upload do arquivo CSV de dados de saúde", type=["csv"])

if data_file is not None:
    df = pd.read_csv(data_file)
    st.success("Arquivo carregado com sucesso!")

    st.subheader("Prévia dos dados")
    st.dataframe(df.head())

    st.subheader("Escolha coluna para análise")
    colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    coluna = st.selectbox("Selecione a coluna numérica para visualizar", colunas_numericas)

    if coluna:
        fig = px.histogram(df, x=coluna, nbins=20, title=f"Distribuição de {coluna}")
        st.plotly_chart(fig)

        st.subheader("Estatísticas básicas")
        st.write(df[coluna].describe())

else:
    st.warning("Por favor, faça upload de um arquivo CSV para começar.")

st.sidebar.markdown("---")
st.sidebar.write("Feito com ❤️ usando Streamlit")