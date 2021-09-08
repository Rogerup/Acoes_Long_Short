import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import streamlit as st  # versão 0.87
import matplotlib.pyplot as plt

st.text('Estratégia Long-Short para Ações (Swing Trade)')

col1, col2, col3 = st.columns(3)
acao1 = col1.text_input('Ação 1:', 'ITUB3')
acao2 = col2.text_input('Ação 2:', 'ITUB4')
period = col3.text_input('Período:', '3y') # (ex: 3y , 12mo)

acao1t = yf.Ticker(acao1 + '.sa')
acao2t = yf.Ticker(acao2 + '.sa')

hist1 = acao1t.history(period=period)
hist2 = acao2t.history(period=period)


fig, ax = plt.subplots()
hist1.Close.plot(ax = ax)
hist2.Close.plot(ax = ax)
st.pyplot(fig)
