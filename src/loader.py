import pandas as pd
import json
import logging
from src.utils import log_exceptions

@log_exceptions
def load_data(paths):
    try:
        sales_df = pd.read_csv(paths['sales'])
        product_df = pd.read_csv(paths['products'])
        with open(paths['stores'], 'r') as f:
            store_data = json.load(f)
        store_df = pd.DataFrame(store_data)

        logging.info("Data loaded successfully.")
        return sales_df, product_df, store_df

    except FileNotFoundError as fnf:
        logging.error(f"File not found: {fnf}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error during data loading: {e}")
        raise