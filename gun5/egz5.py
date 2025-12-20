import streamlit as st
st.title("başlık")
st.write("het türlü veri yazar")
name = st.text_input("ad")
age= st.number_input("yaşinizi girin",min_value=0,max_value=100)
if st.button("gönder"):
    st.write(f"Merhaba {name} nasilsiniz {age} yaşindasiniz")