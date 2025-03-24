import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

df_1 = df.groupby('type')['price'].mean().reset_index()
df_1 = df_1.sort_values(by='price')

df_2 = df.groupby(['manufacturer', 'condition'])['odometer'].mean().reset_index()

df_3 = df['paint_color'].value_counts().reset_index()
df_3.columns = ['paint_color', 'count']

st.header("Vehicle Sales Analysis")

fig = px.histogram(df_1, x="type", y = 'price', color = 'price', title="Average Price per Type of Vehicle")
st.plotly_chart(fig)

fig = px.scatter(df_3, x='paint_color', y='count', title='Scatter Plot of Paint Colors vs. Car Count', size='count', color='paint_color')
st.plotly_chart(fig)
   
if st.checkbox("Show data"):
    st.write(df.head())