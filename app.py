import streamlit as st

st.header("Calculadora", delimiter="gray")


st.write("Expressão")
expression = st.text_input("Entre com os valores")

if (expression):
  result=eval(expression)

  st.write("Resultado:", result)
