# TASK 1 (Predictive Core – Static Time Series Forecasting)
I HAVE USED 2 APPROACHES FOR TASK 1
## Approach 1(LSTM APPROACH)
This project builds a time-series forecasting model for Microsoft (MSFT) stock prices as part of Task 1: The Predictive Core (Static Time Series). Historical daily stock data is downloaded using yfinance and standardized for stable model training. Only the closing price is used for prediction.A rolling window of 29 days is applied to predict the 30th day’s closing price, converting the time series into a supervised learning problem. The model is implemented using a Long Short-Term Memory (LSTM) neural network, which effectively captures both short-term market fluctuations and long-term trends. This approach enables accurate short-term price forecasting from historical data.
## Data
Source: Yahoo Finance (yfinance)

Stock: Microsoft (MSFT)

Feature used: Closing Price

Preprocessing: Standardization

## Method
-Input: 29 consecutive days of closing prices

-Output: 30th day closing price

-Model: LSTM-based neural network

## Results & Metrics
The model is evaluated using Root Mean Squared Error (RMSE).

-Training RMSE: 5.0914

-Testing RMSE: 8.1263

The relatively low RMSE values indicate that the model generalizes well to unseen data while capturing meaningful temporal patterns in stock prices.

## Prediction and visualization
Comparison of actual vs predicted closing prices on the test set, including the confidence interval:

<img width="571" height="453" alt="image" src="https://github.com/user-attachments/assets/263911cf-1af3-4003-9e78-91bf2b38df3d" />

## How to Run

1. **Clone the repository**
```bash
git clone <https://github.com/sanchit1707/GDGTask.git>
cd <using lstm.ipynb>
```
2.**Install dependencies**
```bash
pip install yfinance numpy pandas matplotlib scikit-learn torch
```
3.**Run the notebook**
```bash
jupyter notebook
```
4.**Open and execute using lstm.ipynb cell by cell.**

## Corrections & Further Improvements

### Corrections
- The model currently uses only the **closing price**; future versions can validate results using additional OHLC features.
- Hyperparameters such as **window size (29 days)** and **LSTM hidden units** were selected empirically and can be further tuned.
- Evaluation is limited to **RMSE**; additional metrics can provide better performance insights.


### disadvantages of LSTM
- the model is good with prediction of the overall trend of the closing price but it doesnot incorporate noise.
- it also is not good when used on the difference between the prices of the consecutive days.

i experimented with the transformer based approaches like  chronos-2 and i also tried implimenting transformers from scrach but not able to complete due to time constraints
the time series approaches like ARIMA and SARIMA models gave very less accuracy compared to the LSTM approach and the Chronos-2 model


## Approach 2(Chronos-2 model)

### Time Series Forecasting using Chronos2

## Overview
This project performs **time series forecasting on stock price data** using **Chronos2**, a pretrained transformer-based model for probabilistic forecasting.  
Historical market data is used to predict future closing prices without training a custom model (zero-shot forecasting).

## Data
- **Source:** Yahoo Finance (`yfinance`)
- **Asset:** Stock market data (OHLC)
- **Target Variable:** `Close` price
- **Frequency:** Daily

## Model 
- Chronos2 (Pretrained Transformer)
- Supports probabilistic forecasts (median & quantiles)
- Framework: PyTorch

## prediction
- Forecasts future time steps based on historical context
- Uses median predictions for evaluation
- Generates uncertainty-aware forecasts

## visualization 
- Actual vs Predicted closing prices
- Forecast horizon comparison
- Prediction confidence bands (quantiles)

  <img width="864" height="391" alt="image" src="https://github.com/user-attachments/assets/ed47185f-bbbd-4dcc-90f8-1d5f4a78c3b6" />

## Results & Metrics

Model performance is evaluated on the test set using regression metrics:

test rmse:7.8939

## how to run 

1. **Clone the repository**
```bash
git clone <https://github.com/sanchit1707/GDGTask.git>
cd <>
```
2.**Install dependencies**
```bash
pip install chronos-forecasting yfinance torch pandas numpy matplotlib scikit-learn
```



  


















