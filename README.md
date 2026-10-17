# SmartCart Demo

An original sample shopping cart with stock-aware quantities and TF-IDF
content-based related-product recommendations. No checkout or payment
processing.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Catalog and stock counts are illustrative and are not connected to a merchant.
Test with `python -m unittest discover -s tests -v`.
