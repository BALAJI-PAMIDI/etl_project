def load_data(df):
    """Load data into a CSV file."""
    output_path = "data/posts.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved successfully to {"data/posts.csv"}")
