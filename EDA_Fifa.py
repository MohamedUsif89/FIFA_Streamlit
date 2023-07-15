
import numpy as np
import pandas as pd
import streamlit as st 
import plotly.express as px

st.title('FIFA Exploratory Data Analysis')

st.markdown('This app is a data analysis of the FIFA datase')

fifa = pd.read_csv('fifa_.csv')

st.subheader('Top 5 Valued players')



#st.write(fifa.nlargest(5,'Value')[['Name', 'Value']])

Top_player_Dict = fifa.nlargest(5,'Value')[['Name', 'Value']].set_index('Name').to_dict()

#for name,value in Top_player_Dict['Value'].items():
   # st.markdown(f"+ {name}: {value}")

col1,col2  =st.columns(2)

Histogram = px.histogram(fifa, x='Value', nbins=100)

#Boxplot = px.box(fifa, x='Value', y='Name')
top5 = fifa.nlargest(5, 'Value')[['Name', 'Value']]

col1.write('#### Fifa Top Player')
with col1:
    Top_player_Dict = fifa.nlargest(5,'Value')[['Name', 'Value']].set_index('Name').to_dict()
    for name,value in Top_player_Dict['Value'].items():
        st.markdown(f"+ {name}: {value}")

col2.write('#### Histogram Graph')
with col2:
    fig = px.bar(Top_player_Dict)
    
    st.plotly_chart(Histogram)





