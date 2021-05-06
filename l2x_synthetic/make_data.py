"""
This script contains functions for generating synthetic data. 

Part of the code is based on https://github.com/Jianbo-Lab/CCM
"""
import numpy as np
import pandas as pd


def generate_XOR_labels(X):
    y = np.exp(X[:, 0] * X[:, 1])

    prob_1 = np.expand_dims(1 / (1 + y), 1)
    prob_0 = np.expand_dims(y / (1 + y), 1)

    y = np.concatenate((prob_0, prob_1), axis=1)

    return y


def generate_orange_labels(X):
    logit = np.exp(np.sum(X[:, :4] ** 2, axis=1) - 4.0)

    prob_1 = np.expand_dims(1 / (1 + logit), 1)
    prob_0 = np.expand_dims(logit / (1 + logit), 1)

    y = np.concatenate((prob_0, prob_1), axis=1)

    return y


def generate_additive_labels(X):
    logit = np.exp(
        -100 * np.sin(0.2 * X[:, 0]) + abs(X[:, 1]) + X[:, 2] + np.exp(-X[:, 3]) - 2.4
    )

    prob_1 = np.expand_dims(1 / (1 + logit), 1)
    prob_0 = np.expand_dims(logit / (1 + logit), 1)

    y = np.concatenate((prob_0, prob_1), axis=1)

    return y


def generate_data(n=100, datatype="", seed=0, as_frame=False):
    """
    Generate data (X,y)
    Args:
        n (int): number of samples
        datatype (str): The type of data
            ('orange_skin' | 'XOR' | 'nonlinear_additive' | 'switch')
        seed (int): random seed used
        as_frame (bool): return data as DataFrame.
    Return:
        X (float): [n, d].
        y (float): n dimensional array.
        OR
        df (pd.core.DataFrame): DataFrame containing features with the column names
            {X1, ..., Xp} and targets {Y1, ..., Y2}
    """
    assert datatype in ["orange_skin", "XOR", "nonlinear_additive", "switch"]

    np.random.seed(seed)

    X = np.random.randn(n, 10)

    datatypes = None
    if datatype == "orange_skin":
        y = generate_orange_labels(X)

    elif datatype == "XOR":
        y = generate_XOR_labels(X)

    elif datatype == "nonlinear_additive":
        y = generate_additive_labels(X)

    elif datatype == "switch":

        # Construct X as a mixture of two Gaussians.
        X[: n // 2, -1] += 3
        X[n // 2 :, -1] += -3
        # first n / 2 instances will be "Orange Skin"
        X1 = X[: n // 2]
        # last n / 2 instances will be "Additive Labels"
        X2 = X[n // 2 :]

        y1 = generate_orange_labels(X1)
        y2 = generate_additive_labels(X2)

        # Set the key features of X2 to be the 4-8th features.
        X2[:, 4:8], X2[:, :4] = X2[:, :4], X2[:, 4:8]

        X = np.concatenate([X1, X2], axis=0)
        y = np.concatenate([y1, y2], axis=0)

        # Used for evaluation purposes.
        datatypes = np.array(
            ["orange_skin"] * len(y1) + ["nonlinear_additive"] * len(y2)
        )

        # Permute the instances randomly.
        perm_inds = np.random.permutation(n)
        X, y = X[perm_inds], y[perm_inds]
        datatypes = datatypes[perm_inds]

    if as_frame:
        n, p = X.shape
        feature_names = [f"X{i}" for i in range(1, p + 1)]
        features = pd.DataFrame(X, columns=feature_names)

        n, p = y.shape
        target_names = [f"Y{i}" for i in range(1, p + 1)]
        targets = pd.DataFrame(y, columns=target_names)

        df = features.join(targets)
        df["datatypes"] = datatypes

        return df
    else:
        return X, y
