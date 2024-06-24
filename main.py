# É melhor fazer a análise no python ou no jupyter?
# A resposta é jupyter, pois nos oferece uma estrutura melhor com células e permite uma análise mais eficiente.
# Então, neste terminal, escreve: jupyter-lab

# The challenge:
import streamlit as st
import plotly.express as px
from glob import glob
import nltk

nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

st.title('Diary Tone Analysis')
st.header('Positivity')

filephats: list = glob('diario/*.txt')
diario: list = []
for file in filephats:
    with open(file, encoding='utf-8') as output:
        diario.append(output.read())

analyzer = SentimentIntensityAnalyzer()
score_pos: list = [analyzer.polarity_scores(diario[index])['pos'] for index in range(len(diario))]
score_neg: list = [analyzer.polarity_scores(diario[index])['neg'] for index in range(len(diario))]
date = [date.replace('diario\\.txt', '').removesuffix('.txt').removeprefix('diario\\') for date in filephats]

figure_positive = px.line(x=date, y=score_pos, labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(figure_positive)

st.header('Negativity')

figure_negative = px.line(x=date, y=score_neg, labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(figure_negative)
