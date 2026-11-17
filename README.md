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

## How to run

You need Python 3. The project was tested with Python 3.12, numpy 2.5.5,
pandas 3.1.1, matplotlib 3.11.2 and scipy 1.18.1.

```
git clone https://github.com/DeyvidDimitrov/softuni-task.git
cd softuni-task
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt jupyter
jupyter notebook notebook.ipynb
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

Start Jupyter from the project folder, because the notebook reads
`data/prices.csv` and imports `src/benford.py` from there. Then run all
cells from top to bottom.

To run the whole notebook from the terminal and save the outputs:

```
jupyter nbconvert --to notebook --execute --inplace notebook.ipynb
```

## Functions in src/benford.py

- `clean_prices(df)` - drops missing, non-positive and one-cent prices
- `first_digit(prices)` - first significant digit, for example 0.89 -> 8
- `expected_benford()` - the Benford probabilities for digits 1 to 9
- `compare_to_benford(prices)` - observed and expected counts, chi-square
  statistic and p-value
- `mad(counts)` - mean absolute gap between observed and expected shares
- `cents(prices)` - the cents part of each price, for example 2.99 -> 99
