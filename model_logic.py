import numpy as np
import yfinance as yf
import joblib
from tensorflow import keras
from datetime import datetime, timedelta


def predict_next_close(ticker, lookback=60):
    """
    Predicts the next closing price for a given stock ticker.
    
    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL')
        lookback: Number of days to use for prediction (default: 60)
    
    Returns:
        tuple: (predicted_price, recent_prices_df)
    """
    # Load model and scaler
    model = keras.models.load_model('spy_lstm_model.h5')
    scaler = joblib.load('scaler.save')
    
    # Download recent stock data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=lookback + 30)  # Extra days to ensure we have enough data
    
    stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    if stock_data.empty:
        raise ValueError(f"No data found for ticker {ticker}")
    
    # Get closing prices
    close_prices = stock_data['Close'].values.reshape(-1, 1)
    
    # Ensure we have enough data
    if len(close_prices) < lookback:
        raise ValueError(f"Not enough data. Need at least {lookback} days, got {len(close_prices)}")
    
    # Use the last 'lookback' days for prediction
    recent_prices = close_prices[-lookback:]
    
    # Scale the data
    scaled_prices = scaler.transform(recent_prices)
    
    # Reshape for LSTM: (1, lookback, 1)
    X = scaled_prices.reshape(1, lookback, 1)
    
    # Make prediction
    scaled_prediction = model.predict(X, verbose=0)
    
    # Inverse transform to get actual price
    predicted_price = scaler.inverse_transform(scaled_prediction)[0][0]
    
    # Return prediction and recent history
    recent_df = stock_data[['Close']].tail(lookback).copy()
    recent_df.columns = ['Close']
    
    return predicted_price, recent_df
