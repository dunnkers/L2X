"""
This script contains functions for generating synthetic data. 

Part of the code is based on https://github.com/Jianbo-Lab/CCM
"""
from dataclasses import dataclass
from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd


@dataclass
class DataGenerator:
    name: Optional[str] = None
    n_samples: int = 100
    random_state: Optional[int] = None

    def __post_init__(self):
        np.random.seed(self.random_state)

    def _generate_labels(self, X: np.ndarray) -> np.ndarray:
        ...

    def get_data(self) -> Tuple[np.ndarray, np.ndarray]:
        X = np.random.randn(self.n_samples, 10)
        y = self._generate_labels(X)
        return X, y

    def get_dataframe(self) -> pd.DataFrame:
        X, y = self.get_data()

        n, p = X.shape
        feature_names = [f"X{i}" for i in range(1, p + 1)]
        features = pd.DataFrame(X, columns=feature_names)

        if y is not None:
            n, p = y.shape
            target_names = [f"Y{i}" for i in range(1, p + 1)]
            targets = pd.DataFrame(y, columns=target_names)
            return features.join(targets)
        else:
            return features


@dataclass
class XORGenerator(DataGenerator):
    name: str = "XOR data generator"

    def _generate_labels(self, X: np.ndarray) -> np.ndarray:
        y = np.exp(X[:, 0] * X[:, 1])

        prob_1 = np.expand_dims(1 / (1 + y), 1)
        prob_0 = np.expand_dims(y / (1 + y), 1)

        y = np.concatenate((prob_0, prob_1), axis=1)

        return y


@dataclass
class OrangeGenerator(DataGenerator):
    name: str = "Orange Skin data generator"

    def _generate_labels(self, X: np.ndarray) -> np.ndarray:
        logit = np.exp(np.sum(X[:, :4] ** 2, axis=1) - 4.0)

        prob_1 = np.expand_dims(1 / (1 + logit), 1)
        prob_0 = np.expand_dims(logit / (1 + logit), 1)

        y = np.concatenate((prob_0, prob_1), axis=1)

        return y


@dataclass
class AdditiveGenerator(DataGenerator):
    name: str = "Non-linear Additive data generator"

    def _generate_labels(self, X: np.ndarray) -> np.ndarray:
        logit = np.exp(
            -100 * np.sin(0.2 * X[:, 0])
            + abs(X[:, 1])
            + X[:, 2]
            + np.exp(-X[:, 3])
            - 2.4
        )

        prob_1 = np.expand_dims(1 / (1 + logit), 1)
        prob_0 = np.expand_dims(logit / (1 + logit), 1)

        y = np.concatenate((prob_0, prob_1), axis=1)

        return y


@dataclass
class SwitchGenerator(DataGenerator):
    name: str = "Switch data generator: combines orange labels and non-linear additive"
    orange_generator: DataGenerator = OrangeGenerator()
    additive_generator: DataGenerator = AdditiveGenerator()

    def __post_init__(self):
        np.random.seed(self.random_state)

        self.orange_generator.n_samples = self.n_samples
        self.orange_generator.random_state = self.random_state
        self.additive_generator.n_samples = self.n_samples
        self.additive_generator.random_state = self.random_state

    def get_data(self) -> Tuple[np.ndarray, np.ndarray]:
        n = self.n_samples
        assert n % 2 == 0, "`n_samples` must be divisible by 2."

        X = np.random.randn(self.n_samples, 10)

        # Construct X as a mixture of two Gaussians.
        X[: n // 2, -1] += 3
        X[n // 2 :, -1] += -3
        # first n / 2 instances will be "Orange Skin"
        X1 = X[: n // 2]
        # last n / 2 instances will be "Additive Labels"
        X2 = X[n // 2 :]

        y1 = self.orange_generator._generate_labels(X1)
        y2 = self.additive_generator._generate_labels(X2)

        # Set the key features of X2 to be the 4-8th features.
        X2[:, 4:8], X2[:, :4] = X2[:, :4], X2[:, 4:8]

        X = np.concatenate([X1, X2], axis=0)
        y = np.concatenate([y1, y2], axis=0)

        # Permute the instances randomly.
        perm_inds = np.random.permutation(n)
        X = X[perm_inds]
        y = y[perm_inds]
        self._perm_inds = perm_inds

        return X, y

    def get_dataframe(self):
        df = super().get_dataframe()
        y1_length = self.n_samples // 2
        y2_length = self.n_samples // 2
        datatypes = np.array(
            ["orange_skin"] * y1_length + ["nonlinear_additive"] * y2_length
        )
        datatypes = datatypes[self._perm_inds]
        df["datatypes"] = datatypes
        return df
