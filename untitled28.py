import streamlit as st
import plotly.express as px
import pandas as pd
import json

dados = pd.read_csv('housing.csv')
df = dados.copy()

df.dropna(inplace=True)


eua_states = json.load(open("us-states.json"))

# Opcional: traduzindo as variáveis para o pt
mapa = {'housing_median_age': 'idade da casa',
        'total_rooms': 'quartos',
        'population': 'população',
        'households': 'famílias',
        'median_income': 'renda mediana',
        'median_house_value': 'valor mediano da casa',
        'ocean_proximity': 'Proximidade do mar'}
df.rename(columns = mapa, inplace = True)

categories = list(df['Proximidade do mar'].unique())

# Criei um gráfico de dispersão usando o Plotly
# Documentação: https://plotly.github.io/plotly.py-docs/generated/plotly.express.scatter_mapbox.html
# px.scatter_mapbox é um comando que permite visualizar um gráfico de distribuição em forma de caixa
# 1º especifiquei o dataset df
# 2º após relacionei lat e lon com a primeira e segunda coluna do df
# 3º color='Proximidade do mar', permite com que de acordo com a localidade que para o nosso caso são 5,
# 4º mapbox_style, permite a utilização do mapa aberto
fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="Proximidade do mar",
                        mapbox_style="open-street-map", zoom=3,
                        height=800)

# estou me baseando nesse artigo pra editar a filtragem
### Configurando a visualização no Streamlit
st.title("Análise do Preço por Região\n")
st.write("Vamos ver como o preço de casas na Califórnia varia por região.")

# Filtros para a tabela
mostra_qntd_linhas = 0

checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
if checkbox_mostrar_tabela:

    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(df["Proximidade do mar"].unique())


    categoria = st.sidebar.selectbox('Selecione a região para visualizar o gráfico',
                                 options = categorias)

#if categoria != 'Todas':
    #df['Proximidade do Mar'] = df.query('categoria == @categoria')
    #mostra_qntd_linhas += 1
#else:
    #mostra_qntd_linhas(df)

# Adicione o gráfico ao Streamlit
st.plotly_chart(fig)





