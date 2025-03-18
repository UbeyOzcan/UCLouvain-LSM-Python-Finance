# Python for Finance - Assignment

## Objective
The goal of this assignment is to help you understand how to work with financial data using Python. You will use the `yfinance` library to retrieve stock market data, analyze it, calculate some key financial metrics, and create relevant plots to visualize your findings. This assignment will test your understanding of Python basics, including functions, loops, and data manipulation using `pandas`.

---

## Instructions

### 1. Install Required Libraries
Before starting, make sure you have the necessary libraries installed. You can install them using the following pip commands (pandas for exemple):

```bash
uv pip install pandas
```

### 2. Stock Data Collection
- Write a Python function to download stock data using the `yfinance` library.
- Use the function to collect data for a company of your choice (e.g., Apple - 'AAPL', Tesla - 'TSLA', etc.) for the past 2 years.
- The data should include the following columns: `Open`, `High`, `Low`, `Close`, `Volume`.

#### Function Requirements:
- The function should accept the stock ticker (e.g., 'AAPL') and the date range (start date, end date) as input parameters.
- It should return the stock data as a Pandas DataFrame.

### 3. Data Cleaning
- After downloading the data, check for any missing values and handle them appropriately.
- If there are any missing values in the columns, you can either drop those rows or fill them with the previous valid value (forward fill).
- Display the cleaned data.

### 4. Calculating Key Metrics
Write functions to calculate the following financial metrics:
- **Daily Returns:** Calculate the daily percentage change in the closing price.
- **Moving Average:** Calculate a 30-day simple moving average (SMA) for the closing price.
- **Volatility:** Calculate the rolling 30-day standard deviation of daily returns (a simple measure of volatility).

#### Function Requirements:
- Each function should accept the stock data (DataFrame) as input and return the calculated values.
- You can use `pandas` built-in methods like `pct_change()`, `rolling()`, and `std()` for these calculations.

### 5. Data Visualization
- Plot the closing price of the stock over time.
- Plot the 30-day moving average and the closing price together on the same chart.
- Plot the daily returns as a histogram to visualize the distribution of returns.
- Plot the rolling 30-day volatility (standard deviation) as a line graph.

#### Plotting Requirements:
- Use `matplotlib` or `seaborn` for plotting the charts.
- Label the axes and title the plots appropriately.

### 6. Optional: Correlation Analysis
If you’re feeling adventurous, you can download the stock data of a second company and analyze the correlation between their daily returns.

- Use `pandas` to calculate the correlation between the daily returns of both stocks and plot the correlation matrix as a heatmap.

---

## Deliverables

1. A Python script or Jupyter notebook that includes:
   - Your function to download stock data from Yahoo Finance.
   - Functions to calculate daily returns, moving averages, and volatility.
   - Data cleaning code (handling missing values).
   - Plots visualizing the closing price, moving average, daily returns, and volatility.
   - Any additional analysis or visualizations (optional).

2. A brief write-up summarizing:
   - The company you selected and the time period for the data.
   - The key metrics you calculated and what they represent.
   - Any interesting insights or trends you observed from the plots and analysis.

---


## Additional Notes:
- You can modify the analysis or focus on specific aspects of financial analysis that interest you.
- Be sure to handle any potential errors, such as incorrect ticker symbols or date ranges that return no data.
- The use of functions is encouraged, and make sure your code is clean and well-documented.

---

## Grading Criteria:
- Correct implementation of data downloading function.
- Proper handling of missing data.
- Accurate calculation of the financial metrics.
- Clear and informative plots with appropriate labels.
- Clean and organized code with comments explaining key steps.

Good luck!
