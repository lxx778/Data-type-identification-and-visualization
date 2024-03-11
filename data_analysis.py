import logging
import pandas as pd
import re
from urllib.parse import urlparse
from datetime import datetime

# Helper functions for specific data type checks

def is_integer(series):
    return pd.api.types.is_integer_dtype(series)

def is_float(series):
    return pd.api.types.is_float_dtype(series) and not is_integer(series)

def is_boolean(series):
    if pd.api.types.is_bool_dtype(series):
        return True
    elif series.dropna().isin([0, 1]).all():
        return True
    return False

def is_datetime(series):
    return pd.api.types.is_datetime64_any_dtype(series)

def is_percentage(series):
    if series.dtype == object:
        # Assuming percentages are represented as strings ending with a '%'
        percentage_pattern = re.compile(r"^\s*\d+(\.\d+)?%\s*$")
        return series.str.match(percentage_pattern).all()
    return False

def is_email(series):
    series_str = series.dropna().astype(str)
    return series_str.apply(lambda x: bool(re.match(r"[^@]+@[^@]+\.[^@]+", x))).all()

def is_phone_number(series):
    series_str = series.dropna().astype(str)
    return series_str.apply(lambda x: bool(re.match(r'\+?\d[\d\s()-]+\d$', x))).all()

def is_url(series):
    return series.dropna().apply(lambda x: isinstance(x, str) and bool(urlparse(str(x)).scheme) and bool(urlparse(str(x)).netloc)).all()

def is_categorical(series, cat_threshold=0.05):
    return (len(series.dropna().unique()) / len(series)) < cat_threshold

def is_id(series, id_threshold=0.9):
    series_converted = series.apply(lambda x: str(x) if isinstance(x, (list, dict)) else x)
    unique_ratio = series_converted.nunique() / len(series_converted.dropna())
    return unique_ratio > id_threshold and pd.api.types.is_integer_dtype(series_converted)

def is_numeric(series):
    if pd.to_numeric(series, errors='coerce').notna().all() and not (is_integer(series) or is_float(series)):
        return True
    return False

def is_timestamp(series):
    try:
        numeric_series = pd.to_numeric(series.dropna(), errors='coerce')
        if numeric_series.isna().any():
            return False # Not all values are numeric

        now_timestamp = datetime.now().timestamp()
        min_valid_timestamp = datetime(1970, 1, 1).timestamp()
        max_valid_timestamp = now_timestamp

        return numeric_series.apply(lambda x: min_valid_timestamp <= x <= max_valid_timestamp).all()
    except Exception as e:
        logging.error(f"Error checking for timestamp: {e}")
        return False

    
def is_text(series, length_threshold=50):
    return series.apply(lambda x: len(str(x)) > length_threshold).any()

def is_string(series):
    return series.apply(lambda x: isinstance(x, str)).any()

def is_currency(series):   
    return series.dropna().apply(lambda x: isinstance(x, str) and x.startswith('$')).any()

# Main function to analyze column properties
def analyze_column_properties(df, id_threshold=0.9, cat_threshold=0.05):
    column_properties = {}
    for column in df.columns:
        series = df[column].dropna()  # Drop NA values for analysis
        if series.empty:
            column_properties[column] = 'empty'
            continue
        
        if is_id(series, id_threshold):
            column_properties[column] = 'ID'
        elif is_datetime(series):
            column_properties[column] = 'date'
        elif is_boolean(series):
            column_properties[column] = 'boolean'
        elif is_email(series):
            column_properties[column] = 'email'
        elif is_phone_number(series):
            column_properties[column] = 'phone number'
        elif is_url(series):
            column_properties[column] = 'URL'
        elif is_currency(series):
            column_properties[column] = 'currency'
        elif is_percentage(series):
            column_properties[column] = 'percentage'
        elif is_float(series):
            column_properties[column] = 'float'
        elif is_integer(series):
            column_properties[column] = 'integer'
        elif is_numeric(series):
            column_properties[column] = 'Numeric'
        elif is_text(series):
            column_properties[column] = 'text'
        elif is_string(series):  # Check after other specific string checks to avoid overriding
            column_properties[column] = 'string'
        elif is_categorical(series, cat_threshold):
            column_properties[column] = 'categorical'
        elif is_timestamp(series):  # Ensure numeric checks before timestamp to avoid misclassification
            column_properties[column] = 'timestamp'
        else:
            column_properties[column] = 'unknown'

    return column_properties
