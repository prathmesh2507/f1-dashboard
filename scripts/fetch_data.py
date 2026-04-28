import fastf1
import pandas as pd
import os

fastf1.Cache.enable_cache('data/cache')


def get_latest_completed_race(year=2026):
    schedule = fastf1.get_event_schedule(year)

    # Only completed races
    completed = schedule[schedule['EventDate'] < pd.Timestamp.now()]

    latest = completed.iloc[-1]

    return latest['EventName']


def fetch_race_data(year, gp):
    print(f"Fetching: {gp} {year}")

    session = fastf1.get_session(year, gp, 'R')
    session.load()

    results = session.results
    laps = session.laps

    os.makedirs('data/raw', exist_ok=True)

    results.to_csv(f'data/raw/{year}_{gp}_results.csv', index=False)
    laps.to_csv(f'data/raw/{year}_{gp}_laps.csv', index=False)

    print("Saved successfully ✅")


def fetch_latest_race(year=2026):
    gp = get_latest_completed_race(year)

    # Avoid duplicates
    filename = f"data/raw/{year}_{gp}_results.csv"

    if os.path.exists(filename):
        print("Latest race already exists ✅")
    else:
        fetch_race_data(year, gp)


if __name__ == "__main__":
    fetch_latest_race()