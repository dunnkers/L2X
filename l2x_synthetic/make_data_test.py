import unittest
from make_data import generate_data
import pandas as pd


class TestMakeData(unittest.TestCase):
    def test_generate_data(self):
        X, y = generate_data(n=100, datatype="XOR")
        n, p = X.shape
        assert n == 100
        assert p == 10
        n, p = y.shape
        assert n == 100
        assert p == 2

    def test_dataframe_output(self):
        df = generate_data(n=100, datatype="XOR", as_frame=True)
        assert type(df) == pd.DataFrame


if __name__ == "__main__":
    unittest.main()
