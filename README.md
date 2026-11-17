# Benford's law in Bulgarian retail prices

A small math project. We check if the first digits of retail prices
from Bulgarian store brochures follow Benford's law.

## Layout

- `data/prices.csv` - the prices, with columns `price` and `store`
- `src/benford.py` - the helper functions
- `notebook.ipynb` - the analysis, it imports `src/benford.py`

## Run

```
pip install -r requirements.txt jupyter
jupyter notebook notebook.ipynb
```
