import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter Your Name : ")

age = st.slider("Select your age : ",0,100,25)

st.write(f"Your age is {age}")

options = ['Python','Javascript','C','Java','C++','C#']
choice = st.selectbox("Choose your favorite language : ",options=options)
st.write(f"you selected {choice}.")

if name:
    st.write(f"Hello {name}")


data = {
    "Name":["Jone","Jane","Jake","Jill"],
    "Age":[28,24,35,40],
    "City":["New York","Los Angeles","Chicago","Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)