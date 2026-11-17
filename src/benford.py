"""Helper functions for testing Benford's law on retail prices."""

import numpy as np
import pandas as pd


def expected_probs():
    """Benford probability P(d) = log10(1 + 1/d) for each first digit d = 1..9."""
    digits = np.arange(1, 10)
    return pd.Series(np.log10(1 + 1 / digits), index=digits)


def clean_prices(df):
    """Drop rows where the price is missing, not a number, not positive, or 0.01."""
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    # Prices have at most 2 decimals, so this drops zero, negative and one-cent prices
    df = df[df["price"] > 0.01]
    return df.reset_index(drop=True)
