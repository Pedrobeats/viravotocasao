import streamlit as st
import pandas as pd
import numpy as np

#Lógica
df = pd.read_excel('basevv.xlsx', sheet_name=1)
opcoes_muni = df['MUNICIPIO'].sort_values().unique().tolist()



#Página

st.title('Onde virar votos para o Casão?')

st.markdown('É reta final de eleição! \n \n Aposto que você está com vontade de ir para a rua, conversar com as pessoas e garantir a vitória da democracia com Casagrande. Entretanto, você sabe para onde ir fazer campanha? \n \n Com os dados que disponibilizamos aqui, podemos te ajudar! Criamos um índice que vai de 0 a 1, tipo o IDH: é o **IVV, o Índice de Vira-Voto**. **Quanto mais perto de 1 está o IVV de um bairro, mais vale a pena fazer campanha lá.** \n \n Usando os resultados de votação em cada bairro do país, extraídos e compilados por mim de dados públicos do TRE do Espírito Santo, encontramos os lugares em que há mais eleitores que não votaram em Casagrande no primeiro turno, mas que podem ser convencidos agora.')
st.markdown("O cálculo é feito de maneira simples para encontrar locais que reúnam, simultaneamente, quatro características:")
st.markdown('- Grande número de votos registrados no 1 turno (tamanho do bairro ganhou peso dobrado na pontuação)')
st.markdown('- Grande percentual de eleitores de terceira via que não votaram em Casagrande ou Manato.')
st.markdown('- Grande percentual de eleitores de Casagrande.')
st.markdown('- Pequeno percentual de eleitores de Mannato.')
st.markdown('Para isso, foram usados os dados de votação por bairro de todo o Espírito Santo, extraidos do TRE e de bases abertas e disponíveis a todos os cidadãos. De início, cada bairro do estado foi classificado de acordo com a quantidade de votos. Quanto maior o bairro maior é o impacto de virar votos. Depois, calculou-se a pontuação de cada bairro nas quatro características. É a partir dessa média que o IVV é calculado. Trata-se de uma medida bastante simples que visa encontrar onde são os bairros populosos com um percentual alto de eleitores potencialmente indecisos, mas que moram em áreas propensas a votar em Casagrande. O objetivo é ser uma ferramenta adicional para organizar ações na reta final da campanha, unindo os padrões de votação com o conhecimento cotidiano de quem mora em cada local.')

selecao_municipio = st.selectbox(label="Selecione o seu município", options=opcoes_muni)
df_muni = df[df['MUNICIPIO'].str.match(selecao_municipio)]
st.title(selecao_municipio)


st.dataframe(df_muni, width=2000, height=None, use_container_width=True)
st.title("Todos os bairros do Espírito Santo")
st.dataframe(df, width=2000, height=None, use_container_width=True)

st.caption("O Vira Voto Casão é inspirado na ideia de https://ondevirarvoto.github.io/, como os dados extraidos e filtrados para realidade do ES e webapp refeito em Python")