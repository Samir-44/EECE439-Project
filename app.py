from flask import Flask, request, render_template_string
from model_logic import predict_next_close  # your existing function

app = Flask(__name__)

PAGE = """
<!doctype html>
<html>
  <head>
    <title>LSTM Stock Price Prediction</title>
  </head>
  <body>
    <h1>LSTM Stock Price Prediction</h1>

    <form method="post">
      <label>
        Enter Stock Ticker:
        <input type="text" name="ticker" value="{{ ticker }}" />
      </label>
      <button type="submit">Predict Next Close</button>
    </form>

    {% if error %}
      <p style="color:red;">Error: {{ error }}</p>
    {% endif %}

    {% if predicted_price is not none %}
      <h2>Predicted Next Close for {{ ticker }}: {{ "%.2f"|format(predicted_price) }}</h2>
    {% endif %}

    {% if recent_history is not none %}
      <h3>Recent Price History (last rows)</h3>
      <pre>{{ recent_history }}</pre>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    ticker = ""
    predicted_price = None
    recent_history = None
    error = None

    if request.method == "POST":
        ticker = request.form.get("ticker", "").upper().strip()
        if ticker:
            try:
                predicted_price, recent_history = predict_next_close(ticker)
                # recent_history is a pandas Series/DataFrame; convert to text
                recent_history = recent_history.tail(10).to_string()
            except Exception as e:
                error = str(e)
        else:
            error = "Please enter a ticker symbol."

    return render_template_string(
        PAGE,
        ticker=ticker,
        predicted_price=predicted_price,
        recent_history=recent_history,
        error=error,
    )

if __name__ == "__main__":
    # local run only; Azure uses gunicorn
    app.run(host="0.0.0.0", port=8000, debug=True)
