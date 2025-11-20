import streamlit as st
import pandas as pd
from model_logic import predict_next_close


st.title("📈 Stock Price Prediction")

# Input for ticker
ticker = st.text_input("Enter Stock Ticker:", value="AAPL")

# Prediction button
if st.button("Predict Next Close"):
    try:
        with st.spinner(f"Fetching data and predicting for {ticker}..."):
            predicted_price, recent_history = predict_next_close(ticker)
        
        # Display prediction
        st.success(f"**Predicted Next Close:** ${predicted_price:.2f}")
        
        # Plot recent price history
        st.subheader("Recent Price History")
        st.line_chart(recent_history)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
