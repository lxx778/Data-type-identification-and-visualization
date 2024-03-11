def output_data_types(data_types):
    """
    Output the data types of each column.

    Parameters:
    data_types (dict): A dictionary with column names as keys and their data types as values.
    """
    for column, dtype in data_types.items():
        print(f"Column: {column}, Type: {dtype}")
