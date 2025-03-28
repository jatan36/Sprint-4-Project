import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")
df['manufacturer'] = df['model'].str.split(' ', n=1).str[0].str.upper()

# GRAPH 1 - VEHICLE TYPE VS AVERAGE PRICE
df_1 = df.groupby(['type'])['price'].mean().reset_index()
df_1 = df_1.sort_values(by='price')

fig = px.histogram(df_1, x="type", y = 'price', color = 'price', title="Average Price per Type of Vehicle")
fig.update_xaxes(title_text="Car Type")
fig.update_yaxes(title_text="Average Price")
st.plotly_chart(fig)

# GRAPH 2 - CAR CONDITION VS ODOMETER PER CAR MANUFACTURER
df = df[df['odometer'] != 'Unknown']
df['odometer'] = df['odometer'].astype(float)
df_2 = df.groupby(['manufacturer','condition'])['odometer'].mean().reset_index().sort_values(by = 'odometer')

fig = px.histogram(df_2, x="manufacturer", y ='odometer', color ='condition', title ='Condition vs Odometer per Manufacturer')
fig.update_xaxes(title_text="Car Manufacturer")
fig.update_yaxes(title_text="Number of Miles")
st.plotly_chart(fig)

# GRAPH 3 - CAR COLOR VS AVERAGE PRICE
df_3 = df.groupby('paint_color')['price'].mean().reset_index()
df_4 = df['paint_color'].value_counts().reset_index()
df_4.columns = ['paint_color', 'count']
df_color = df_3.merge(df_4).sort_values(by = 'count', ascending = False)

fig = px.scatter(df_color, x='paint_color', y='price', size='count', color='count', title='Color Popularity vs Price')
fig.update_xaxes(title_text="Paint Color")
fig.update_yaxes(title_text="Average Price of Car")
st.plotly_chart(fig)

# Header of the Project
st.header("Project 4: Vehicle Sales Analysis")

# Checkbox
if st.checkbox("Show Dataset"):
    print(df)