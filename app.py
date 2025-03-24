import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")
df['manufacturer'] = df['model'].str.split(' ', n=1).str[0].str.upper()

df_1 = df.groupby('type')['price'].mean().reset_index()
df_1 = df_1.sort_values(by='price')

df_2 = df.groupby(['manufacturer', 'condition'])['odometer'].mean().reset_index()

df_3 = df['paint_color'].value_counts().reset_index()
df_3.columns = ['paint_color', 'count']

st.header("Vehicle Sales Analysis")

# Average Cost of Vehicle per Vehicle Type
fig = px.histogram(df_1, x="type", y = 'price', color = 'price', title="Average Price per Type of Vehicle")
fig.update_xaxes(title_text="Car Type")
fig.update_yaxes(title_text="Average Price")
st.plotly_chart(fig)

# Average Miles per Car Condition
fig = px.histogram(df_2, x="manufacturer", y = 'odometer', color = 'condition', title="Average Miles vs Car Condition for each Manufacturer")
fig.update_xaxes(title_text="Car Manufacturer")
fig.update_yaxes(title_text="Average Miles")

# Popular Car Colors
fig = px.scatter(df_3, x='paint_color', y='count', title= 'Most Popular Car Colors', size='count', color='paint_color')
fig.update_layout(xaxis_title='Paint Color', yaxis_title='Count of Cars')
st.plotly_chart(fig)
   
if st.checkbox("Show data"):
    st.write(df.head())