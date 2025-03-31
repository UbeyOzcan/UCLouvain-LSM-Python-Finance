import pandas as pd
import numpy as np

def ptf_simulation(ptf_return:pd.DataFrame, nsim:int=10000, rfr:float=0.01) -> pd.DataFrame:
    n_stocks = len(ptf_return.columns)
    sim_df = pd.DataFrame(index=range(nsim), columns=range(n_stocks))
    sim_df.columns = ptf_return.columns
    sim_df['return'] = None
    sim_df['sigma'] = None
    for i in range(nsim):
        sim_df.iloc[i,0:n_stocks] = np.random.rand(n_stocks)
        sim_df.iloc[i,0:n_stocks] = sim_df.iloc[i,0:n_stocks]/sim_df.iloc[i,0:n_stocks].sum()
        sim_df.iloc[i,2] = np.sum(sim_df.iloc[i,0:n_stocks] * ptf_return.mean()) * 252
        sim_df.iloc[i,3] = np.sqrt(np.dot(sim_df.iloc[i,0:n_stocks].T, np.dot(ptf_return.cov() * 252, sim_df.iloc[i,0:n_stocks])))
    sim_df.insert(loc=len(sim_df.columns), column='sharpe-ratio', value=(sim_df['return'] - rfr)/sim_df['sigma'])
    return sim_df
