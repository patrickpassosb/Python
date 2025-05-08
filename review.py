import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book Review", page_icon=":book:", layout="wide")

st.title("Book Review")
st.subheader("Customer Reviews")
df_reviews = pd.read_csv('customer reviews.csv')
df_top100_books = pd.read_csv('Top-100 Trending Books.csv')

df_reviews
df_top100_books