import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import streamlit.components.v1 as components

arquivo_csv = "database-tradingview.csv"  
df = pd.read_csv(arquivo_csv)

df_texto = df.to_string(index=False)

def home():
    st.title("Home")
    st.header("👋 Bem-vindo ao App de Monitoramento Trade Ideas no TradingView! 🚀")
    st.subheader("Com nossa ferramenta, você terá acesso a:")
    st.info("💬 Ativos e Tópicos em Destaque: Saiba quais ativos estão gerando mais discussões e descubra os cinco principais termos em torno deles.")
    st.info("📈 Estatísticas de Recomendações: Fique por dentro das estatísticas das recomendações feitas por traders, permitindo que você avalie insights valiosos.")
    st.info("🌟 Traders Influentes: Identifique os traders mais influentes da comunidade, aqueles com mais seguidores e recomendações.")
    st.info("🔥 Tópicos em Alta: Explore os tópicos mais populares em nossa comunidade. Descubra os 10 títulos mais curtidos sobre o ativo de sua escolha.")
    st.write("Seja bem-vindo ao App. 💼📊💰")

def top_5_termos():
    st.title("Modelagem de Tópicos - Top 5 termos dos tópicos mais comentados")

    idioma = ["Inglês", "Português"]
    idioma_selecionado = st.selectbox("Selecione um Idioma:", idioma)

    if idioma_selecionado == "Inglês":
       imagem = st.image("images/baseingles.png", caption="Base em inglês", use_column_width=True)
    else:
        imagem = st.image("images/baseportugues.png", caption="Base em português", use_column_width=True)
    
def top_5_termos_ativos():
    ticker_counts = df['Ticker'].value_counts().head(5)
    tickers_top_5 = ticker_counts.index.tolist()

    ativo_selecionado = st.selectbox("Selecione um Ativo:", tickers_top_5)

    if ativo_selecionado == "BTCUSD":
      imagem = st.image("images/btcusd.png", caption="BTCUSD", use_column_width=True)
    if ativo_selecionado == "BTCUSDT":
      imagem = st.image("images/btcusdt.png", caption="BTCUSDT", use_column_width=True)
    if ativo_selecionado == "EURUSD":
      imagem = st.image("images/eurusd.png", caption="EURUSD", use_column_width=True)
    if ativo_selecionado == "XAUUSD":
      imagem = st.image("images/xauusd.png", caption="XAUUSD", use_column_width=True)
    if ativo_selecionado == "BTCUSDT.P":
      imagem = st.image("images/btcusdtp.png", caption="BTCUSDT.P", use_column_width=True)
  
def estatistica_recomendacoes():
    st.title("Estatísticas de recomendações")

    ativos = df['Ticker'].unique()
    ativo_selecionado = st.selectbox("Selecione um Ativo:", ativos)

    if ativo_selecionado:
        df_ativo = df[df['Ticker'] == ativo_selecionado]

        total_vies_baixa = df_ativo[df_ativo['Recommendation'] == 'Viés de baixa']['Recommendation'].count()
        total_vies_alta = df_ativo[df_ativo['Recommendation'] == 'Viés de alta']['Recommendation'].count()

        total_recomendacoes = len(df_ativo)

        if total_recomendacoes > 0:
            porcentagem_vies_baixa = (total_vies_baixa / total_recomendacoes) * 100
            porcentagem_vies_alta = (total_vies_alta / total_recomendacoes) * 100

            total_porcentagens = porcentagem_vies_baixa + porcentagem_vies_alta

            if total_porcentagens != 100:
                proporcao_vies_baixa = porcentagem_vies_baixa / total_porcentagens
                proporcao_vies_alta = porcentagem_vies_alta / total_porcentagens

                porcentagem_vies_baixa = proporcao_vies_baixa * 100
                porcentagem_vies_alta = proporcao_vies_alta * 100

            st.write(f"Quantidade de 'Viés de Baixa': {total_vies_baixa}")
            st.write(f"Porcentagem Ajustada de 'Viés de Baixa': {porcentagem_vies_baixa:.2f}%")
            st.write(f"Quantidade de 'Viés de Alta': {total_vies_alta}")
            st.write(f"Porcentagem Ajustada de 'Viés de Alta': {porcentagem_vies_alta:.2f}%")
        else:
            st.write("Não há recomendações para este ativo.")

def ativos_mais_comentados():  
    st.title("Ativos mais comentados")  

    if 'Ticker' in df.columns:
        contagem_tickers = df['Ticker'].value_counts()
        top_10_tickers = contagem_tickers.head(10)

        st.write("Os 10 ativos mais comentados:")
        st.write(top_10_tickers.index)  #Mostra os nomes dos tickers
    else:
        st.write("A coluna 'Ticker' não foi encontrada no DataFrame.")

def usuarios_mais_seguidores():
    df_sorted = df.drop_duplicates(subset=['Trader'])
    df_sorted = df_sorted.sort_values(by='Seguidores', ascending=False)

    st.title("Traders com Mais Seguidores")
    st.write(df_sorted[['Trader', 'Seguidores']])


def usuarios_maior_recomendacoes():
    recommendation_counts = df['Trader'].value_counts().reset_index()
    recommendation_counts.columns = ['Trader', 'Contagem de recomendações']

    recommendation_counts_sorted = recommendation_counts.sort_values(by='Contagem de recomendações', ascending=False)

    st.title("Traders com Mais Recomendações")
    st.table(recommendation_counts_sorted[['Trader', 'Contagem de recomendações']])

def titulos_mais_curtidos():
  ativos = df['Ticker'].unique()

  st.title("Top 10 Títulos Mais Curtidos por Ativo")
  ativo_selecionado = st.selectbox("Selecione um Ativo:", ativos)

  if ativo_selecionado:
    df_ativo = df[df['Ticker'] == ativo_selecionado]

    df_ativo_sorted = df_ativo.sort_values(by='Likes', ascending=False)
    top_10_titulos = df_ativo_sorted[['Title', 'Likes']].head(10)
    st.write(top_10_titulos)

def posts_mais_recentes():
  ativos = df['Ticker'].unique()
  st.title("Posts Mais Recentes por Ativo")
  ativo_selecionado = st.selectbox("Selecione um Ativo:", ativos)

  if ativo_selecionado:
    df_ativo = df[df['Ticker'] == ativo_selecionado]
    df_ativo = df_ativo[df_ativo['Date'] != 'Atualizado']
    df_ativo_sorted = df_ativo.sort_values(by='Date', ascending=False)
    st.write(df_ativo_sorted[['Date', 'Title', 'Content']])

def posts_atualizados():
  ativos = df['Ticker'].unique()

  st.title("Posts Mais Atualizados por Ativo")
  ativo_selecionado = st.selectbox("Selecione um Ativo:", ativos)

  if ativo_selecionado:
    df_ativo = df[(df['Ticker'] == ativo_selecionado) & (df['Update'] != 'Atualizado')]
    df_ativo['Update'] = pd.to_datetime(df_ativo['Update'], errors='coerce')

    df_ativo['Update'].fillna('Atualizado', inplace=True)

    df_ativo_sorted = df_ativo.sort_values(by='Update', ascending=False)
    st.write(df_ativo_sorted[['Update','Date', 'Title', 'Content']])


def main():
    st.sidebar.title("App de Monitoramento Trade Ideas do TradingView")
    st.sidebar.image('images/logo.png', width=300)
    st.sidebar.markdown('---')
    lista_menu = ["Home",  "Modelagem de Tópicos - Top 5 termos dos tópicos mais comentados", "Modelagem de Tópicos - Top 5 termos dos ativos mais comentados", "Estatísticas de recomendações", "Ativos mais comentados",
    "Traders com mais seguidores", "Traders com mais recomendações", "Os 10 títulos mais curtidos do ativo escolhido", "Estatísticas de recomendações", "Ativos mais comentados",
    "Traders com mais seguidores", "Traders com mais recomendações", "Os 10 títulos mais curtidos do ativo escolhido",
    "Posts mais recentes do ativo escolhido", "Posts mais atualizados do ativo escolhido"] 
    escolha = st.sidebar.radio('Escolha uma opção', lista_menu)

    if escolha == 'Home':
        home()
    if escolha == 'Modelagem de Tópicos - Top 5 termos dos tópicos mais comentados':
        top_5_termos()
    if escolha == 'Modelagem de Tópicos - Top 5 termos dos ativos mais comentados':
        top_5_termos_ativos()
    if escolha == 'Estatísticas de recomendações':
       estatistica_recomendacoes()
    if escolha == 'Ativos mais comentados':  
        ativos_mais_comentados()  
    if escolha == 'Traders com mais seguidores':
        usuarios_mais_seguidores()
    if escolha == 'Traders com mais recomendações':
        usuarios_maior_recomendacoes()
    if escolha == 'Os 10 títulos mais curtidos do ativo escolhido':
        titulos_mais_curtidos()
    if escolha == 'Posts mais recentes do ativo escolhido':
        posts_mais_recentes()
    if escolha == 'Posts mais atualizados do ativo escolhido':
        posts_atualizados()

if __name__ == "__main__":
    main()