import fastf1
import pandas as pd
import os

# Enable cache
fastf1.Cache.enable_cache('data/cache')

def fetch_race_data(year, gp):
    print(f"Fetching data for {gp} {year}...")

    session = fastf1.get_session(year, gp, 'R')
    session.load()

    # Race Results
    results = session.results

    # Lap Data
    laps = session.laps

    # Create folders if not exist
    os.makedirs('data/raw', exist_ok=True)

    # Save files
    results.to_csv(f'data/raw/{year}_{gp}_results.csv', index=False)
    laps.to_csv(f'data/raw/{year}_{gp}_laps.csv', index=False)

    print("Data saved successfully ✅")


if __name__ == "__main__":
    fetch_race_data(2025, 'Monaco')  # test race