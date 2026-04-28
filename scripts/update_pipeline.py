from fetch_data import fetch_latest_race
from preprocess import process_all
import os
import fastf1

# Create cache directory if it doesn't exist
cache_dir = 'data/cache'
os.makedirs(cache_dir, exist_ok=True)

# Now enable the cache
fastf1.Cache.enable_cache(cache_dir)


def run_pipeline():
    print("🚀 Starting Auto Pipeline...")

    fetch_latest_race(2026)
    process_all()

    print("✅ Pipeline completed")


if __name__ == "__main__":
    run_pipeline()