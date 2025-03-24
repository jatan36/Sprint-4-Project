import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Vehicle Sales Analysis")

fig = px.histogram(df, x="price")
st.plotly_chart(fig)

fig = px.scatter(df, x="type", y="price")
st.plotly_chart(fig)
   
if st.checkbox("Show data"):
    st.write(df.head())