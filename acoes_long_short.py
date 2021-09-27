import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import streamlit as st  # versão 0.87
import matplotlib.pyplot as plt

# st.title/header/subheadr/text
st.subheader('Estratégia Long-Short para Ações (Swing Trade)')
st.text('')

col1, col2, col3 = st.columns(3)
acao1 = col1.text_input('Ação 1:', 'ITUB4')
acao2 = col2.text_input('Ação 2:', 'ITUB3')
period = col3.text_input('Período (ex: 2y , 6mo, 45d):', '3y')

acao1t = yf.Ticker(acao1 + '.sa')
acao2t = yf.Ticker(acao2 + '.sa')

# Carrega o histórico das ações
hist1 = acao1t.history(period=period)
hist2 = acao2t.history(period=period)

# Calcula as razões entre as ações
hist_ratio = (hist1.Close/hist2.Close).mean()

min_ratio = (hist1.Close/hist2.Close).min()
max_ratio = (hist1.Close/hist2.Close).max()

acao1_preco_atual = hist1.Close.tail(1)[0]
acao2_preco_atual = hist2.Close.tail(1)[0]

pres_ratio = acao1_preco_atual / acao2_preco_atual
var_perc = (pres_ratio-hist_ratio) / hist_ratio * 100

# Colunas com as exibições das razões entre as duas ações
col_his, col_min, col_max, col_pre = st.columns(4)
col_his.metric('Razão Histórica:', f'{hist_ratio:0.3f}')
col_min.metric('Razão Mínima:', f'{min_ratio:0.3f}',
                f'{(min_ratio-hist_ratio) / hist_ratio * 100:0.1f}%')
col_max.metric('Razão Máxima:', f'{max_ratio:0.3f}',
                f'{(max_ratio-hist_ratio) / hist_ratio * 100:0.1f}%')
col_pre.metric('Razão Atual:', f'{pres_ratio:0.3f}', f'{var_perc:0.1f}%')

st.text('')

# Verifica qual está melhor para comprar e vender
if pres_ratio < hist_ratio:
    acao_compra, acao_compra_preco = acao1, acao1_preco_atual
    acao_venda, acao_venda_preco   = acao2, acao2_preco_atual
else:
    acao_compra, acao_compra_preco = acao2, acao2_preco_atual
    acao_venda, acao_venda_preco   = acao1, acao1_preco_atual

# Colunas com indicação de compra/venda
col_c, col_cp, col_v, col_vp = st.columns(4)
col_c.metric('Indicação: COMPRA', acao_compra)
col_cp.subheader(f'R$ {acao_compra_preco:0.2f}')
col_v.metric('Indicação: VENDA',  acao_venda)
col_vp.subheader(f'R$ {acao_venda_preco:0.2f}')

# Alguns testes de apresentação não utilizados
# col_c, col_v = st.columns(2)
# col_c.metric('Indicação: COMPRA', acao_compra, f'R$ {acao_compra_preco:0.2f}', 'off')
# col_v.metric('Indicação: VENDA',  acao_venda,  f'R$ {acao_venda_preco:0.2f}',  'off')
# col_c.metric('Indicação: COMPRA', f'{acao_compra}  ({acao_compra_preco:0.2f})')
# col_v.metric('Indicação: VENDA',  f'{acao_venda}  ({acao_venda_preco:0.2f})')
# col_c.metric('Indicação: COMPRA', f'{acao_compra}')
# col_v.metric('Indicação: VENDA',  f'{acao_venda}')
# col_cp, col_vp = st.columns(2)
# col_cp.subheader(f'R$ {acao_compra_preco:0.2f}')
# col_vp.subheader(f'R$ {acao_venda_preco:0.2f}')

# Gráfico das duas ações
fig, ax = plt.subplots()
hist1.Close.plot(ax = ax)
hist2.Close.plot(ax = ax)
ax.legend([acao1, acao2])
st.pyplot(fig)

# Observação final
st.text('')
st.text('')
st.text('OBSERVAÇÃO:')
st.text('Este dashboard é apenas para o estudo básico do Streamlit.')
st.text('NUNCA O UTILIZE PARA OPERAÇÕES REAIS !!!')
st.text('')
st.text('')
st.text('A título de curiosidade, ações ON/PN normalmente apresentam')
st.text('uma boa correlação para visualizar nos gráficos:')
st.text('Ex: ITUB3/ITUB4, BBDC3/BBDC4, SAPR3/SAPR4, PETR3/PETR4')
st.text('Ou empresas do mesmo setor:')
st.text('Ex: ITUB4/BBDC4, LREN3/LAME4')
st.text('.')
