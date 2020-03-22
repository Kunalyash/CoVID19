# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:59:55 2020

@author: KUNAL V
"""

import pandas as pd
import plotly.express as px
from plotly.offline import plot

path = r'C:\Users\KUNAL V\Downloads'
#path = os.getcwd() (Store code and xlsx file in same folder)
df = pd.read_excel(path + "\\" + "covid_19_data.xlsx")  
df.rename(columns = {'Country/Region':'Country'}, inplace =True)
df_1 = df[df.Country != 'Mainland China']
df_2 = df.groupby('ObservationDate').sum().reset_index()
df_2 = df_2.drop(['SNo'], axis =1)
df_3 = pd.read_excel(path + "\\" + "covid_19_data.xlsx", usecols = ('ObservationDate','Deaths',"Country/Region"))
df_3.rename(columns = {'Country/Region':'Country'}, inplace =True)
df_4 = df_3[df_3.Country != 'Mainland China'] 
df_test = df.groupby('Country')['Deaths'].agg('sum').reset_index()


"""
Block A:
    The following snippet of code will generate the Bar Chart of Reported Death Across the countries
"""

figure = px.bar(df, x='Country', y = 'Deaths', color='Country', title ='Reported Deaths Across Countries')
plot(figure)

figure = px.bar(df_1, x='Country', y = 'Deaths', color='Country', title ='Reported Deaths Across Countries(Excluding China)')
plot(figure)
"""
Block B:
    The following code will show the piechart distribution of COVID-19 affected countries.
"""

figure = px.pie(df, values='Confirmed', names='Country',title='Infected Rates Across countries',hover_data=['Province/State'], labels={'Province/State':'Province/State'})
figure.update_traces(textposition='inside')
plot(figure)

figure = px.pie(df_1, values='Confirmed', names='Country',title='Infected Rates Across countries(Excluding China)',hover_data=['Province/State'], labels={'Province/State':'Province/State'})
figure.update_traces(textposition='inside')
plot(figure)
"""
Block C:
   The following code will show scatter plot of COVID-19 affected Countries
"""

fig = px.scatter(df_3, x="ObservationDate", y="Deaths", title ="Scatter Plot of Deaths in Affected Countries" )
plot(fig)

fig = px.scatter(df_4, x="ObservationDate", y="Deaths", title ="Scatter Plot of Deaths in Affected Countries(Excluding China)")
plot(fig)

"""
Block D:
    Statistics of recovery, death and total affected people in COVID-19 affected countries
"""
print (df['Deaths'].describe())
print (df['Recovered'].describe())
print (df['Confirmed'].describe())




