import unittest

import numpy as np
import pandas as pd

from l2x_synthetic import (
    AdditiveGenerator,
    DataGenerator,
    OrangeGenerator,
    SwitchGenerator,
    XORGenerator,
)


class TestMakeData(unittest.TestCase):
    def test_data_generator(self):
        gen = DataGenerator(n_samples=1, random_state=None)
        X, y = gen.get_data()
        assert np.shape(X) == (1, 10)
        assert y == None

        X_, y_ = gen.get_data()
        assert not np.isclose(
            X, X_
        ).any(), (
            "random_state=None should yield different data every `get_data()` call."
        )

    def test_dataframe_output(self):
        gen = DataGenerator(n_samples=1, random_state=0)
        df = gen.get_dataframe()
        assert type(df) == pd.DataFrame
        assert (
            df.columns
            == [
                "X1",
                "X2",
                "X3",
                "X4",
                "X5",
                "X6",
                "X7",
                "X8",
                "X9",
                "X10",
            ]
        ).all()

    def test_xor(self):
        gen = XORGenerator(n_samples=1, random_state=0)
        X, y = gen.get_data()
        X_true = [
            [
                1.76405235,
                0.40015721,
                0.97873798,
                2.2408932,
                1.86755799,
                -0.97727788,
                0.95008842,
                -0.15135721,
                -0.10321885,
                0.4105985,
            ]
        ]
        y_true = [[0.66949419, 0.33050581]]
        assert np.isclose(X, X_true).all()
        assert np.isclose(y, y_true).all()

    def test_orange_skin(self):
        gen = OrangeGenerator(n_samples=1, random_state=0)
        X, y = gen.get_data()
        X_true = [
            [
                1.76405235,
                0.40015721,
                0.97873798,
                2.2408932,
                1.86755799,
                -0.97727788,
                0.95008842,
                -0.15135721,
                -0.10321885,
                0.4105985,
            ]
        ]
        y_true = [[0.99478785, 0.00521215]]
        assert np.isclose(X, X_true).all()
        assert np.isclose(y, y_true).all()

    def test_nonlinear_additive(self):
        gen = AdditiveGenerator(n_samples=1, random_state=0)
        X, y = gen.get_data()
        X_true = [
            [
                1.76405235,
                0.40015721,
                0.97873798,
                2.2408932,
                1.86755799,
                -0.97727788,
                0.95008842,
                -0.15135721,
                -0.10321885,
                0.4105985,
            ]
        ]
        y_true = [[3.94704563e-16, 1.00000000e00]]
        assert np.isclose(X, X_true).all()
        assert np.isclose(y, y_true).all()

    def test_switch(self):
        gen = SwitchGenerator(n_samples=2, random_state=0)
        X, y = gen.get_data()
        X_true = [
            [
                1.76405235,
                0.40015721,
                0.97873798,
                2.2408932,
                1.86755799,
                -0.97727788,
                0.95008842,
                -0.15135721,
                -0.10321885,
                3.4105985,
            ],
            [
                0.14404357,
                1.45427351,
                0.76103773,
                0.12167502,
                0.14404357,
                1.45427351,
                0.76103773,
                0.12167502,
                0.3130677,
                -3.85409574,
            ],
        ]
        y_true = [[0.99478785, 0.00521215], [0.10158596, 0.89841404]]
        assert np.isclose(X, X_true).all()
        assert np.isclose(y, y_true).all()

    def test_switch_dataframe_output(self):
        gen = SwitchGenerator(n_samples=2, random_state=0)
        df = gen.get_dataframe()
        assert df["datatypes"] is not None
        assert df["datatypes"].values[0] == "orange_skin"


if __name__ == "__main__":
    unittest.main()
