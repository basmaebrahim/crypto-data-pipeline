📈 Crypto Data Pipeline
Description

This Python project is a Crypto Data Pipeline that automatically fetches cryptocurrency data from an API, transforms and cleans it, performs basic analysis, and generates visualizations of top cryptocurrencies by market cap, price, and 24h price change.

The pipeline is fully automated and saves outputs in organized folders for easy access.

Project Structure
crypto_pipeline/
│
├─ main.py                # Main script to run the pipeline
├─ requirements.txt       # Python dependencies
├─ data/
│   ├─ raw/               # Raw data fetched from API (CSV)
│   └─ processed/         # Processed data and charts (PNG)
├─ pipeline/
│   ├─ extract_api.py     # API data extraction functions
│   ├─ transform.py       # Data cleaning & transformation functions
│   └─ load_analysis.py   # Analysis functions (top 5 metrics)
├─ visualizations/
│   └─ charts.py          # Functions to plot charts
└─ README.md
Features
Fetch live crypto data from API
Clean and transform raw data
Save raw and processed data in CSV
Analyze top 5 cryptocurrencies by:
Market Cap
Price
24h Price Change
Generate visual charts:
Market Cap chart (marketcap.png)
Price chart (price.png)
24h Change chart (change.png)
Installation
Clone the repository:
git clone <your-repo-url>
cd crypto_pipeline
Install dependencies:
pip install -r requirements.txt
Usage

Run the pipeline:

python main.py

Outputs will be saved in:

data/raw/crypto_raw.csv
data/processed/marketcap.png
data/processed/price.png
data/processed/change.png
Dependencies
Python 3.10+
pandas
matplotlib
requests
logging

(Install via pip install -r requirements.txt)

Example Output

Top 5 Cryptos by Market Cap:

id	symbol	current_price	market_cap
bitcoin	btc	69,569	1,395,426,825,201
ethereum	eth	2,130	257,654,950,307
tether	usdt	0.999	184,115,850,886
binancecoin	bnb	609.65	83,232,034,593
ripple	xrp	1.33	81,671,532,644

Charts are automatically saved in data/processed/.

License

MIT License – free to use and modify.