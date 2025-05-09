import streamlit as st
import pandas as pd


st.set_page_config(page_title="Book Review", page_icon=":book:", layout="wide")

st.title("Book Review")
st.subheader("Customer Reviews")

df_reviews = pd.read_csv('customer reviews.csv')
df_top100_books = pd.read_csv('Top-100 Trending Books.csv')

price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()

max_price = st.sidebar.slider("Select the price range", min_value=price_min , max_value=price_max, value=(price_min, price_max))
df_books = df_top100_books[(df_top100_books['book price'] >= max_price[0]) & (df_top100_books['book price'] <= max_price[1])]
df_books
