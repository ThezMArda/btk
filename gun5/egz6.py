import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = st.file_uploader("csv",type=["csv"])
st.title("histogram gösterici")

if file:
    df= pd.read_csv(file)
    st.write("yüklenen veri")
    st.write(df)
    numeric_cols=df.select_dtypes(include =["int64","float64"]).columns
    column = st.selectbox("histogram için bir sütün seçiniz",numeric_cols)

    if column:
        fig , ax =plt.subplots()
        ax.hist(df[column],alpha =.7)
        ax.set_title("columnlarin histogrami")
        ax.set_ylabel("frekans")
        st.pyplot(fig)
    