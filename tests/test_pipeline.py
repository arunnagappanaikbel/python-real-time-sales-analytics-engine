# tests/test_pipeline.py
import pytest
import pandas as pd
from src.transformer import transform_data
from src.analyser import analyze_data
from src.config_loader import load_config
from src.loader import load_data
import os

CONFIG = load_config("config/config.yaml")

def test_load_data():
    sales_df, product_df, store_df = load_data(CONFIG['data_paths'])
    assert not sales_df.empty
    assert not product_df.empty
    assert not store_df.empty
    assert 'product_id' in sales_df.columns

def test_transform_data():
    sales_df, product_df, store_df = load_data(CONFIG['data_paths'])
    transformed_df = transform_data(sales_df, product_df, store_df)
    assert 'total' in transformed_df.columns
    assert 'high_value' in transformed_df.columns
    assert pd.api.types.is_datetime64_any_dtype(transformed_df['sale_date'])

def test_analyze_data(tmp_path):
    # Prepare transformed data
    sales_df, product_df, store_df = load_data(CONFIG['data_paths'])
    transformed_df = transform_data(sales_df, product_df, store_df)
    output_file = tmp_path / "test_output.csv"
    analyze_data(transformed_df, str(output_file))

    # Check that file was created and contains expected columns
    assert output_file.exists()
    df = pd.read_csv(output_file)
    assert 'total_sales' in df.columns
    assert 'avg_quantity' in df.columns
    assert 'high_value_sales' in df.columns
