"""Helper functions for testing Benford's law on retail prices."""

import pandas as pd


def clean_prices(df):
    """Drop rows where the price is missing, not a number, not positive, or 0.01."""
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    # Prices have at most 2 decimals, so this drops zero, negative and one-cent prices
    df = df[df["price"] > 0.01]
    return df.reset_index(drop=True)
