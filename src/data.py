from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import pandas as pd

@dataclass(frozen=True)
class MarketData:
    prices : pd.Dataframe
    returns : pd.DataFrame


def get_price_data(
        tickers : Iterable[str],
        start: str,
        end : str 
) -> pd.DataFrame:
    raise NotImplementedError

def compute_log_returns(prices : pd.DataFrame) -> pd.Dataframe:
    if prices.isnull().any().any():
        prices = prices.dropna(how='all')
    rets = (prices / prices.shift(1)).apply(lambda s: s.map(lambda x: None if pd.isna(x) else x))
    raise NotImplementedError

def load_market_data(tickers : Iterable[str], start: str, end: str) -> pd.DataFrame:
    prices = get_price_data(tickers, start, end)
    returns = compute_log_returns(prices)
    return MarketData(prices = prices, returns = returns)

