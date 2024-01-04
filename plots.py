import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
import numpy as np
import streamlit as st
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header("Visualise Data")
  st.set_option("deprecation.showPyplotGlobalUse",False)
  st.subheader("Scatter Plot") 
  features_list = st.multiselect("select the x-axis values:", ("carwidth", "enginesize", "horsepower", "drivewheel_fwd", "car_company_buick"))
  for i in features_list:
    st.subheader(f'Scatter Plot between {i} and price')
    plt.figure(figsize=(12,5))
    sns.scatterplot(x=i, y='price', data=car_df)
    st.pyplot()
  st.subheader("Visualisation Selector")
  plot_types = st.multiselect("select charts or plots:", ('Histogram', 'BoxPlot','Correlation Heatmap'))
  if 'Histogram' in plot_types:
    st.subheader("Histogram")
    columns = st.selectbox("select the column to create its histogram", ("carwidth", "enginesize", "horsepower"))
    plt.figure(figsize=(12,5))
    plt.hist(car_df[columns], bins='sturges', edgecolor='black')
    st.pyplot()

  if 'BoxPlot' in plot_types:
    st.subheader("BoxPlot")
    columns = st.selectbox("select the column to create its boxplot", ("carwidth", "enginesize", "horsepower"))
    plt.figure(figsize=(12,5))
    sns.boxplot(car_df[columns])
    st.pyplot()

  if 'Correlation Heatmap' in plot_types:
    st.subheader('Correlation Heatmap')
    plt.figure(figsize=(12,5))
    ax = sns.heatmap(car_df.corr(), annot=True)
    bottom,top = ax.get_ylim()
    ax.set_ylim(bottom+0.5, top-0.5)
    st.pyplot()