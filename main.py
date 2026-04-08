from pipeline.extract_api import extract
from pipeline.transform import transform
from pipeline.load_analysis import load_and_analyze
from visualizations.charts import (
    plot_top5_marketcap,
    plot_top5_price,
    plot_top5_change
)

import logging
from logger import setup_logger

def run_pipeline():
    setup_logger()
    logging.info("Starting Crypto Data Pipeline...\n")

    extract()
    transform()
    load_and_analyze()

    # 👇
    plot_top5_marketcap()
    plot_top5_price()
    plot_top5_change()

    logging.info("\n Pipeline Finished Successfully!")


if __name__ == "__main__":
    run_pipeline()