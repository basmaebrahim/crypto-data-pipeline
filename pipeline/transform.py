import pandas as pd
from pathlib import Path
import logging

def transform():
    logging.info("Starting Transformation...")

    raw_path = Path(__file__).parent.parent / "data" / "raw" / "crypto_raw.csv"
    df = pd.read_csv(raw_path)
    logging.info(f"Raw data loaded: {df.shape[0]} rows")
    columns_needed = [
        "id",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]

    df_clean = df[columns_needed]
    df_clean = df_clean.dropna()
    df_clean.reset_index(drop=True, inplace=True)
    
    # clear minus values
    df = df[df["current_price"] > 0]
    df = df[df["market_cap"] > 0]

    # 🔹 Feature Engineering
    df["price_change_category"] = df["price_change_percentage_24h"].apply(
        lambda x: "High Gain" if x > 5 else
                  "Gain" if x > 0 else
                  "Loss"
    )
    df = df.sort_values(by="market_cap", ascending=False)

    # 🔹add ranking 
    df["rank"] = range(1, len(df) + 1)
    processed_path = Path(__file__).parent.parent / "data" / "processed" / "crypto_clean.csv"
    processed_path.parent.mkdir(parents=True, exist_ok=True)

    df_clean.to_csv(processed_path, index=False)

    logging.info(f"Transform done: {df.shape[0]} clean records saved")