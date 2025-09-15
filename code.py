import streamlit as st
from currency_converter import CurrencyConverter

# Initialize converter
c = CurrencyConverter()

st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

st.title("💱 Currency Converter")

amount = st.number_input("Enter amount:", min_value=0.0, value=100.0)

col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("From Currency", sorted(c.currencies), index=sorted(c.currencies).index("USD"))
with col2:
    to_currency = st.selectbox("To Currency", sorted(c.currencies), index=sorted(c.currencies).index("INR"))

if st.button("Convert"):
    try:
        result = c.convert(amount, from_currency, to_currency)
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        st.error(f"Error: {e}")
