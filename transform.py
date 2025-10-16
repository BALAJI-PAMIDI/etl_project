import pandas as pd

def transform_data(data):
    """Clean and transform extracted data."""
    df = pd.DataFrame(data)
    df = df[['userId', 'id', 'title', 'body']]
    df['title'] = df['title'].str.title()
    return df
