import numpy as np
import pandas as pd
from src.utils import log_exceptions
import logging

@log_exceptions
def analyze_data(df, output_path):
    logging.info("Starting analysis...")
    
    summary = df.groupby(['region', 'category']).agg(
        total_sales=('total', 'sum'),
        avg_quantity=('quantity', 'mean'),
        high_value_sales=('high_value', lambda x: (x == 'Yes').sum())
    ).reset_index()
    
    try:
        summary.to_csv(output_path, index=False)
        logging.info(f"Analysis written to {output_path}")
    except Exception as e:
        logging.error(f"Failed to write analysis: {e}")
        raise