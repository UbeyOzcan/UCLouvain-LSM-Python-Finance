from src.datafactory import get_closing, stock_return
from src.modelfactory import ptf_simulation
import plotly.express as px

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices = get_closing(ticker=['AAPL', 'NFLX'], start_dt='2024-01-01', end_dt='2024-12-31')
    return_df = stock_return(prices).dropna()
    simulation = ptf_simulation(return_df, nsim=10000)
    fig = px.scatter(x=simulation['sigma'], y=simulation['return'])
    fig.write_html("file.html")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
