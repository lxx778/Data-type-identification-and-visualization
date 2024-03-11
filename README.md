# ASRM555_hw2_mingxi3

This tool identifies data types for each column in a dataset and performs comprehensive exploratory data analysis, presenting statistics and visualizations.

## Setup

Instructions on setting up the project:

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Create a virtual environment:
   - Unix-based systems: `python3 -m venv venv`
   - Windows: `python -m venv venv`
4. Activate the virtual environment:
   - Unix-based systems: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
5. Install dependencies: If you are in the project directory, you can simply run:
   `pip install -r requirements.txt ` 
   If you are not in the project directory, specify the full path to the requirements.txt file:
   `pip install -r /path/to/requirements.txt`



## Running the Script

1. To run the main script, use the following command:
   `python main.py "/path/to/your/dataset.csv" `
   If you are not in the project directory, please add the path to main.py
2. After getting the datatype type you will be asked "Would you like to perform exploratory data analysis on the  dataset? (y/n)", replying with y will give you the html file that opens with the default browser and contains the Descriptive and plots. At the same time, the file will be saved in the project directory.


