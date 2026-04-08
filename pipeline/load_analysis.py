import pandas as pd
from pathlib import Path
import logging
def load_and_analyze():
    processed_path = Path(__file__).parent.parent / "data" / "processed" / "crypto_clean.csv"
    df = pd.read_csv(processed_path)

    print("\nTop 5 by Market Cap:")
    print(df.sort_values(by="market_cap", ascending=False).head(5))

    print("\nTop 5 by Price:")
    print(df.sort_values(by="current_price", ascending=False).head(5))

    print("\nTop 5 by 24h Change:")
    print(df.sort_values(by="price_change_percentage_24h", ascending=False).head(5))

    logging.info("Load & Analysis done")