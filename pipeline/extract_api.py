import requests
import pandas as pd
from pathlib import Path
import yaml
import logging
import time  # for retry

def extract():
    # config file path
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"

    # read congig.YAML file
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    base_url = config['crypto_api']['base_url']
    endpoint = config['crypto_api']['coins_endpoint']
    currency = config['crypto_api']['currency']
    per_page = config['crypto_api'].get('per_page', 10)
    page = config['crypto_api'].get('page', 1)

    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page,
        "sparkline": False
    }

    #  3 Retry mechanism:ـ API
    for attempt in range(3):
        try:
            logging.info(f"Attempt {attempt+1}: Fetching data from API...")
            response = requests.get(base_url + endpoint, params=params, timeout=10)
            response.raise_for_status()  # يرفع exception لو فيه خطأ HTTP
            break
        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt+1} failed: {e}")
            time.sleep(2)  # wait 2 seconds before second retry

    else:
        raise Exception("API request failed after 3 attempts")

    # convert to DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # save raw data 
    raw_path = Path(__file__).parent.parent / "data" / "raw" / "crypto_raw.csv"
    raw_path.parent.mkdir(parents=True, exist_ok=True)  

    # save data
    
    df.to_csv(raw_path, index=False)
    logging.info(f"Extract done: {len(df)} records saved to {raw_path}")
