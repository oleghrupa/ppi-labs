from dataloader.coinbaseloader import CoinbaseLoader, Granularity

import pandas as pd

class TestClass:

    @classmethod
    def setup_class(cls):
        cls._loader = CoinbaseLoader()

    def test_get_pairs(self):
        data = self._loader.get_pairs()
        assert data is not None and len(data) != 0, "Empty pairs list received"
        assert isinstance(data, pd.DataFrame), "Pandas DataFrame expected"
        assert "BTC" in data.base_currency.values, "BTC base currency not found"

    def test_get_stats(self):
        pass

    def test_get_historical_data(self):
        pass
