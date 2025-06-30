import pandas as pd
import numpy as np
import logging
import json
from src.utils import log_exceptions

@log_exceptions
def transform_data(sales_df, product_df, store_df):
    logging.info(f'Starting transformations...')
    
    #Handling missing null
    sales_df['quantity'].fillna(0, inplace=True)
    sales_df['price'].fillna(sales_df['price'].mean(), inplace=True)
    
    #calculate total sales
    sales_df['total'] = sales_df['price'] * sales_df['quantity']
    
    #Merge with product and store info
    merged_df = sales_df.merge(product_df, on="product_id", how='left')
    merged_df = merged_df.merge(store_df, on="store_id", how='left')
    
    #convert sale_date to datetime
    merged_df['sale_date'] = pd.to_datetime(merged_df['sale_date'])
    
    # Create new columns using numpy
    merged_df['high_value'] = np.where(merged_df['total'] > 50, 'Yes', 'No')
    
    #Fill any remaining missing value
    merged_df.fillna({'product_name':'unknown', 'category':'unknown', 'region':'unknown'},inplace=True)
    
    #Pivot table total sales by region
    pivot_df = merged_df.pivot_table(
        index='region',
        columns='category',
        values='total',
        aggfunc='sum',
        fill_value=0
    )
    
    logging.info("Transformation completed.")
    return merged_df
    
