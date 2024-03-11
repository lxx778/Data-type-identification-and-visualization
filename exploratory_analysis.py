import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import webbrowser
import os

def exploratory_data_analysis(df):
    # Start HTML content with descriptive statistics
    stats = df.describe(include='all').to_html()
    html_content = f"<html><head><h1>Descriptive Statistics</h1></head><body>{stats}<hr><h1>Plots</h1>"

    # Subplot settings for improved visualization
    fig = make_subplots(rows=len(df.columns), cols=1, subplot_titles=df.columns, vertical_spacing=0.02)
    for i, column in enumerate(df.columns):
        if pd.api.types.is_numeric_dtype(df[column]):
            fig.add_trace(go.Histogram(x=df[column], name=column), row=i+1, col=1)
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column), row=i+1, col=1)
        else: # Categorical data
            counts = df[column].value_counts()
            fig.add_trace(go.Bar(x=counts.index, y=counts.values, name=column), row=i+1, col=1)

    # Update layout for better readability
    fig.update_layout(height=500*len(df.columns), width=1500)
    html_content += f"<div>{fig.to_html(full_html=False)}</div>"
    html_content += "</body></html>"

    with open('exploratory_data_analysis_report.html', 'w') as f:
        f.write(html_content)
    
    file_path = 'exploratory_data_analysis_report.html'
    absolute_file_path = 'file://' + os.path.realpath(file_path)
    webbrowser.open(absolute_file_path)

if __name__ == "__main__":
    df = pd.read_csv("your_dataset.csv")  # Change this to your dataset path
    exploratory_data_analysis(df)
