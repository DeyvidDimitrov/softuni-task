"""Helper functions for testing Benford's law on retail prices."""

import pandas as pd


def clean_prices(df):
    """Drop rows where the price is missing, not a number, or not positive."""
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    df = df[df["price"] > 0]
    return df.reset_index(drop=True)
