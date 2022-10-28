#### "O Vira Voto Casão é inspirado na ideia de https://ondevirarvoto.github.io/, como os dados extraidos e filtrados para realidade do ES e webapp refeito em Python usando o Streamlit.

# Onde virar votos para o Casão?

É reta final de eleição! Aposto que você está com vontade de ir para a rua, conversar com as pessoas e garantir a vitória da democracia com Casagrande. Entretanto, você sabe para onde ir fazer campanha? Com os dados que disponibilizamos aqui, podemos te ajudar! 

Criamos um índice que vai de 0 a 1, tipo o IDH: é o **IVV, o Índice de Vira-Voto**. **Quanto mais perto de 1 está o IVV de um bairro, mais vale a pena fazer campanha lá.** Usando os resultados de votação em cada bairro do país, extraídos e compilados por mim de dados públicos do TRE do Espírito Santo, encontramos os lugares em que há mais eleitores que não votaram em Casagrande no primeiro turno, mas que podem ser convencidos agora.

O cálculo é feito de maneira simples para encontrar locais que reúnam, simultaneamente, quatro características:
- Grande número de votos registrados no 1 turno (tamanho do bairro ganhou peso dobrado na pontuação.
- Grande percentual de eleitores de terceira via que não votaram em Casagrande ou Manato.
- Grande percentual de eleitores de Casagrande.
- Pequeno percentual de eleitores de Mannato.

Para isso, foram usados os dados de votação por bairro de todo o Espírito Santo, extraidos do TRE e de bases abertas e disponíveis a todos os cidadãos. De início, cada bairro do estado foi classificado de acordo com a quantidade de votos. Quanto maior o bairro maior é o impacto de virar votos. Depois, calculou-se a pontuação de cada bairro nas quatro características. É a partir dessa média que o IVV é calculado. Trata-se de uma medida bastante simples que visa encontrar onde são os bairros populosos com um percentual alto de eleitores potencialmente indecisos, mas que moram em áreas propensas a votar em Casagrande. O objetivo é ser uma ferramenta adicional para organizar ações na reta final da campanha, unindo os padrões de votação com o conhecimento cotidiano de quem mora em cada local.
