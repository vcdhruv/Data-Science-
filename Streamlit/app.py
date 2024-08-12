import streamlit as st
import pandas as pd
import numpy as np


## Title of the application
st.title("Hello Streamlit!")

## Display a simple text
st.write("This is a simple text.")

## Create a simple dataframe
df = pd.DataFrame({
    'first column' : [1,2,3,4,5],
    'second column' : [6,7,8,9,10]
})

## Displaying a simple dataframe
st.write(df)


## Creating a line chart
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])

## Displaying a line chart
st.line_chart(chart_data)
