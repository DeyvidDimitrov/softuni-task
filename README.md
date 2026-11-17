# Benford's law in Bulgarian retail prices

A small math project. We check if the first digits of retail prices from
Bulgarian store brochures follow Benford's law, and what the gaps tell us
about how stores set prices.

## What is inside

- `notebook.ipynb` - the analysis: problem, theory, data, method, results,
  experiments, limitations and conclusion
- `src/benford.py` - the functions the notebook uses
- `data/prices.csv` - brochure prices from 12 stores, collected by shopi.bg,
  with columns `price` and `store`
- `requirements.txt` - the Python packages

## Functions in src/benford.py

- `clean_prices(df)` - drops missing, non-positive and one-cent prices
- `first_digit(prices)` - first significant digit, for example 0.89 -> 8
- `expected_benford()` - the Benford probabilities for digits 1 to 9
- `compare_to_benford(prices)` - observed and expected counts, chi-square
  statistic and p-value
- `mad(counts)` - mean absolute gap between observed and expected shares
- `cents(prices)` - the cents part of each price, for example 2.99 -> 99
