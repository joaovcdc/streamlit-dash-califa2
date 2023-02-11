import streamlit as st
import plotly.express as px
import pandas as pd
import json

dados = pd.read_csv('housing.csv')
df = dados.copy()

df.dropna(inplace=True)


#eua_states = json.load(open("us-states.json"))

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

# estou me baseando nesse artigo pra editar a filtragem
### Configurando a visualização no Streamlit
st.title("Análise do Preço por Região\n")
st.write("Vamos ver como o preço de casas na Califórnia varia por região.")

# Filtros para a tabela
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela') # Se estiver selecionado no streamlit
if checkbox_mostrar_tabela:

    st.sidebar.markdown('## Filtro para a tabela') # mostra as possibilidades de filtro (near bay, the ocean, inland, near ocean, island)

    categorias = list(df["Proximidade do mar"].unique()) #cria uma opção com todas as categorias
    categorias.append('Todas') # Adiciona todas, para caso queira ver todas as regiões pintadas no streamlit depois

    categoria = st.sidebar.selectbox('Selecione a região para visualizar o gráfico',
                                     options = categorias)
    # 1º Filtrar os dados
    # 2º Fazer figura de acordo com o dado filtrado
    # 3º Aplicar ao streamlit

    if categoria != 'Todas': # Se a categoria no selectbox que criei for diferente de todas, seleciona a categoria escolhida
        df = df.loc[df["Proximidade do mar"] == categoria] # cria um dataframe com a categoria escolhida, que vai ser utilizado na fig
    else:
        pass

    # px.scatter_mapbox é um comando que permite visualizar um gráfico de distribuição em forma de caixa
    # 1º especifiquei o dataset df
    # 2º após relacionei lat e lon com a primeira e segunda coluna do df
    # 3º color='Proximidade do mar', permite com que de acordo com a localidade que para o nosso caso são 5, faça uma cor pra cada local
    # 4º mapbox_style, permite a utilização do mapa aberto

    df['valor_mediano_da_casa'] = 'R$ ' + df['valor mediano da casa'].astype(str)

    colors = ['purple', 'gray', 'pink', 'red', 'green'] # lista de cores
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color = "Proximidade do mar", text = df['valor_mediano_da_casa']
                            ,mapbox_style="open-street-map", zoom=3, color_discrete_sequence = colors,
                            height=800)

    # Adicione o gráfico ao Streamlit
    st.plotly_chart(fig)

# A figura precisa ficar depois da filtragem, pois a figura que queremos visualizar pode variar com o selectbox escolhido




