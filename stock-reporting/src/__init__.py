import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import numpy as np


class ExcelReporter:
    def __init__(self, tckr: str) -> None:
        self.tckr = tckr
        self.data = self.get_close()

    def get_close(self) -> pd.DataFrame:
        return yf.Ticker(self.tckr).history(period="1y")

    def scatter_close(self) -> go.Figure:
        if 'Close' not in self.data.columns:
            raise Exception('Close column not found')

        date = self.data.index
        close = self.data['Close']

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=date, y=close, name="linear", line_shape='linear'))
        return fig


    def scatter_dailyreturn(self) -> go.Figure:
        if 'Close' not in self.data.columns:
            raise Exception('Close column not found')
        self.data['Daily Return'] = np.log(self.data['Close'] / self.data['Close'].shift(1))
        date = self.data.index
        r = self.data['Daily Return']
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=date, y=r, name="linear", line_shape='linear'))
        return fig

    def metrics(self) -> pd.DataFrame:
        if 'Close' not in self.data.columns:
            raise Exception('Close column not found')

        self.data['Daily Return'] = np.log(self.data['Close'] / self.data['Close'].shift(1))
        metrics = self.data['Daily Return'].agg(['mean', 'std'])
        return metrics

    def create_report(self) -> None:
        df = self.data.reset_index(drop=False)
        df['Date'] = df['Date'].apply(lambda a: pd.to_datetime(a).date())
        metrics = self.metrics()
        with pd.ExcelWriter(f'Reporting/{self.tckr}.xlsx') as writer:
            df.to_excel(writer, sheet_name='data')
            metrics.to_excel(writer, sheet_name='metrics')

        fig_scatter_close = self.scatter_close()
        fig_scatter_close.write_html(f'Reporting/{self.tckr}_closing_price.html')
        fig_scatter_dailyreturn = self.scatter_dailyreturn()
        fig_scatter_dailyreturn.write_html(f'Reporting/{self.tckr}_daily_log_return.html')
