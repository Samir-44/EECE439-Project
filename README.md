# LSTM Stock Price Predictor

A web application that uses a pre-trained LSTM (Long Short-Term Memory) neural network to predict the next closing price of stocks. Built with Streamlit for an intuitive user interface.

## Features

- Predict next-day closing prices for any stock ticker
- Interactive web interface
- Visual chart of recent price history (last 60 days)
- Real-time data fetching using yfinance

## Project Structure

```
├── app.py                  # Main Streamlit web application
├── model_logic.py          # Prediction logic and data processing
├── spy_lstm_model.h5       # Pre-trained LSTM model
├── scaler.save             # Data scaler for normalization
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Samir-44/EECE439-Project.git
cd EECE439-Project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Make Predictions

1. Enter a stock ticker symbol in the text input (e.g., AAPL, MSFT, SPY)
2. Click the **"Predict Next Close"** button
3. View the predicted next closing price
4. Examine the chart showing the last 60 days of historical prices

## How It Works

1. **Data Collection**: Downloads the last 60+ days of closing prices using yfinance
2. **Data Preprocessing**: Normalizes prices using the pre-trained scaler
3. **Prediction**: Feeds the normalized sequence into the LSTM model
4. **Output**: Returns the predicted next-day closing price and displays historical data

## Example Stock Tickers

### Tech Companies
- **AAPL** - Apple Inc.
- **MSFT** - Microsoft Corporation
- **GOOGL** - Alphabet Inc. (Google)
- **AMZN** - Amazon.com Inc.
- **META** - Meta Platforms Inc.
- **NVDA** - NVIDIA Corporation
- **TSLA** - Tesla Inc.

### Index ETFs
- **SPY** - SPDR S&P 500 ETF Trust
- **QQQ** - Invesco QQQ Trust (NASDAQ-100)
- **DIA** - SPDR Dow Jones Industrial Average ETF

### Financial
- **JPM** - JPMorgan Chase & Co.
- **V** - Visa Inc.
- **BAC** - Bank of America Corp.

## Requirements

- Python 3.8 or higher
- TensorFlow
- Streamlit
- yfinance
- pandas
- numpy
- scikit-learn
- joblib

See `requirements.txt` for specific versions.

## Model Details

- **Architecture**: LSTM (Long Short-Term Memory)
- **Input**: 60 days of closing prices
- **Output**: Next day's closing price prediction
- **Training Data**: Historical S&P 500 data

## Limitations

- Predictions are based solely on historical price patterns
- Does not account for news, events, or fundamental analysis
- Past performance does not guarantee future results
- Requires at least 60 days of trading history for a stock

## License

This project is for educational purposes.

## Author

Samir-44

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Stock data from [yfinance](https://pypi.org/project/yfinance/)
- Deep learning framework: [TensorFlow](https://www.tensorflow.org/)
