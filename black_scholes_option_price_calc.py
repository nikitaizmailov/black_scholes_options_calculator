import streamlit as st
import numpy as np
from scipy.stats import norm

# Black-Scholes Options Pricing model calculator
st.subheader("Options Pricing Calculator to calculate a Fair Price of the Option")

with st.container():
    st.write("Black-Scholes Option Pricing Model")
    ### Black Scholes model
    # Current stock (or other underlying) price

    S = (st.text_input("Current Stock Price", 30.5))

    # Strike price
    K = (st.text_input("Strike Price of the option", 60))

    # risk free interest rate
    r = (st.text_input("10 year risk free interest rate (1.4 for 1.4%)", 1.4))

    # time to maturity
    t = (st.text_input("time to maturity in days", 394))

    # Standard Deviation σ same as Implied Volatility for the option
    sigma = (st.text_input("Implied Volatility (40 for 40%, 55 for 55%)", 44))

    option_type = st.selectbox("Select Option Type (Call/Put)", ['Call', "Put"])

# Black-Schloles formula/function
def black_scholes_model(r, S, K, t, sigma, option_type):
    """Calculate BS option price for a call/put"""
    # checking if value is a string or None
    S = float(S)
    K = float(K)
    r = float(r) / 100
    t = float(t) / 365
    sigma = float(sigma) /100
    d1 = (np.log(S/K) + (r + sigma**2/2)*t)/(sigma*np.sqrt(t))
    d2 = d1 - sigma*np.sqrt(t)
    if (option_type == "Call"):
        price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*t)*norm.cdf(d2, 0, 1)
    elif (option_type == "Put"):
        price = K*np.exp(-r*t)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
    return st.write(f"Fair Option Price: {price}")

st.button('Generate Fair Price of Stock Option', on_click=black_scholes_model(r, S, K, t, sigma, option_type))

