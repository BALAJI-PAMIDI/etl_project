from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    print("🔹 Extracting data...")
    raw_data = extract_data()

    print("🔹 Transforming data...")
    transformed = transform_data(raw_data)

    print("🔹 Loading data...")
    load_data(transformed)

    print("🎉 ETL pipeline completed successfully!")

if __name__ == "__main__":
    run_etl()
