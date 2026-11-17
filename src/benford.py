"""Helper functions for testing Benford's law on retail prices."""

import numpy as np
import pandas as pd
from scipy import stats


def clean_prices(df):
    """Drop rows where the price is missing, not a number, not positive, or 0.01."""
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    # Prices have at most 2 decimals, so this drops zero, negative and one-cent prices
    df = df[df["price"] > 0.01]
    return df.reset_index(drop=True)


def first_digit(prices):
    """First significant digit of each positive number, for example 0.89 -> 8."""
    # Read the digit from the text, because math on floats can be off:
    # 0.3 / 0.1 is 2.9999999999999996, which would give 2 instead of 3.
    text = pd.Series(prices, dtype=float).astype(str)
    return text.str.lstrip("0.").str[0].astype(int)


def expected_benford():
    """Benford probability P(d) = log10(1 + 1/d) for each first digit d = 1..9."""
    digits = np.arange(1, 10)
    return pd.Series(np.log10(1 + 1 / digits), index=digits)


def compare_to_benford(prices):
    """Observed and expected first-digit counts, chi-square statistic and p-value."""
    digits = first_digit(prices)
    observed = digits.value_counts().reindex(range(1, 10), fill_value=0)
    expected = len(digits) * expected_benford()
    chi2, p = stats.chisquare(observed, expected)
    counts = pd.DataFrame({"observed": observed, "expected": expected})
    counts.index.name = "digit"
    return counts, chi2, p


def mad(counts):
    """Mean absolute gap between observed and expected shares (Nigrini's MAD)."""
    shares = counts / counts.sum()
    return (shares["observed"] - shares["expected"]).abs().mean()


def cents(prices):
    """The cents part of each price as a whole number, for example 2.99 -> 99."""
    # Round first, because 0.29 * 100 is 28.999999999999996
    return np.round(pd.Series(prices, dtype=float) * 100).astype(int) % 100
