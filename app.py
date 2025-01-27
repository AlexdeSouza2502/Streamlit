import streamlit as st

st.header("Calculadora", divider="gray")

expression = st.text_input("Entre com a expressão")

if (expression):
  result = eval(expression)

  st.write("Resultado: ", result)
