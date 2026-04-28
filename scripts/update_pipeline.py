from fetch_data import fetch_latest_race
from preprocess import process_all


def run_pipeline():
    print("🚀 Starting Auto Pipeline...")

    fetch_latest_race(2026)
    process_all()

    print("✅ Pipeline completed")


if __name__ == "__main__":
    run_pipeline()