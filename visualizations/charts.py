import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import logging


def load_data():
    path = Path(__file__).parent.parent / "data" / "processed" / "crypto_clean.csv"
    return pd.read_csv(path)


def plot_top5_marketcap():
    df = load_data()
    top5 = df.sort_values(by="market_cap", ascending=False).head(5)

    plt.figure()
    plt.bar(top5["symbol"], top5["market_cap"])
    plt.title("Top 5 Cryptos by Market Cap")
    plt.xlabel("Crypto")
    plt.ylabel("Market Cap")

    output_path = Path(__file__).parent.parent / "data" / "processed" / "marketcap.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_path)
    plt.close()

    logging.info(f"Market Cap chart saved to {output_path}")


def plot_top5_price():
    df = load_data()
    top5 = df.sort_values(by="current_price", ascending=False).head(5)

    plt.figure()
    plt.bar(top5["symbol"], top5["current_price"])
    plt.title("Top 5 Cryptos by Price")

    output_path = Path(__file__).parent.parent / "data" / "processed" / "price.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_path)
    plt.close()

    logging.info(f"Price chart saved to {output_path}")


def plot_top5_change():
    df = load_data()
    top5 = df.sort_values(by="price_change_percentage_24h", ascending=False).head(5)

    plt.figure()
    plt.bar(top5["symbol"], top5["price_change_percentage_24h"])
    plt.title("Top 5 Cryptos by 24h Change")

    output_path = Path(__file__).parent.parent / "data" / "processed" / "change.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_path)
    plt.close()

    logging.info(f"Change chart saved to {output_path}")