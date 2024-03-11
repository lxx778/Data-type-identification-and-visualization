import unittest
from unittest.mock import patch
import io
from input_data import read_dataset
from data_analysis import analyze_column_properties
from output_type import output_data_types
import pandas as pd

class TestDatasetTypeIdentifier(unittest.TestCase):
    def setUp(self):
        self.test_dataframe = pd.DataFrame({
            'integers': [1, 2, 3],
            'floats': [1.1, 2.2, 3.3],
            'strings': ['a', 'b', 'c'],
            'emails': ['test@example.com', 'hello@world.com', None],
            'phone_numbers': ['123-456-7890', '+1-234-567-8901', ''],
            'urls': ['http://example.com', 'https://www.example.com', None],
            'booleans': [True, False, True],
            'dates': pd.to_datetime(['2021-01-01', '2022-02-02', None]),
            'percentages': ['25%', '50%', '75%']
        })

    def test_read_dataset(self):
        # Assuming read_dataset is properly defined to read a DataFrame for testing
        # You should replace this with actual reading from a file if necessary
        dataset = read_dataset(self.test_dataframe)  # Mocked for example purposes
        self.assertIsInstance(dataset, pd.DataFrame)

    def test_analyze_column_properties(self):
        data_types = analyze_column_properties(self.test_dataframe)
        expected_types = {
            'integers': 'integer',
            'floats': 'float',
            'strings': 'text',  # Assuming default for strings is text
            'emails': 'email',
            'phone_numbers': 'phone number',
            'urls': 'URL',
            'booleans': 'boolean',
            'dates': 'date',
            'percentages': 'percentage'
        }
        self.assertEqual(data_types, expected_types)

    def test_output_data_types(self):
        data_types = {'test': 'integer'}
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            output_data_types(data_types)
            self.assertIn('Column: test, Type: integer', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()