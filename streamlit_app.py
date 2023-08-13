import streamlit as st
import pandas as pd
import yfinance as yf
st.title("İlk Cloud Streamlit Projem")

btc=yf.download("BTC-USD","2008-01-01","2023-08-12")

st.table(btc)
