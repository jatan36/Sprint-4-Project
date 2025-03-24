import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Vehicle Sales Analysis")

fig = px.histogram(df_1, x="type", y = 'price', color = 'price', title="Average Price per Type of Vehicle")
st.plotly_chart(fig)

fig = px.scatter(df_3, x='paint_color', y='count', title='Scatter Plot of Paint Colors vs. Car Count', size='count', color='paint_color')
st.plotly_chart(fig)
   
if st.checkbox("Show data"):
    st.write(df.head())