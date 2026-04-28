from fetch_data import fetch_race_data
from preprocess import process_all

def run_pipeline():
    year = 2025
    gp = 'Monaco'

    print("Starting pipeline...")

    fetch_race_data(year, gp)
    process_all()

    print("Pipeline completed successfully 🚀")


if __name__ == "__main__":
    run_pipeline()