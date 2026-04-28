import pandas as pd
import os


# -----------------------------
# 🏁 CLEAN RACE RESULTS
# -----------------------------
def clean_results(file_path):
    df = pd.read_csv(file_path)

    df = df[[
        'DriverNumber',
        'FullName',
        'TeamName',
        'Position',
        'Points',
        'GridPosition',
        'Status'
    ]]

    df.columns = [
        'driver_number',
        'driver',
        'team',
        'position',
        'points',
        'grid_position',
        'status'
    ]

    return df


# -----------------------------
# 🛞 CLEAN LAP DATA (ADVANCED)
# -----------------------------
def clean_laps(file_path):
    df = pd.read_csv(file_path)

    # Drop invalid laps
    df = df.dropna(subset=['LapTime'])

    # Convert time columns to seconds (important for analysis)
    time_cols = [
        'LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time',
        'PitInTime', 'PitOutTime'
    ]

    for col in time_cols:
        if col in df.columns:
            df[col] = pd.to_timedelta(df[col], errors='coerce').dt.total_seconds()

    # Select meaningful columns
    df = df[[
        'Driver',
        'DriverNumber',
        'LapNumber',
        'LapTime',
        'Sector1Time',
        'Sector2Time',
        'Sector3Time',
        'Compound',
        'TyreLife',
        'FreshTyre',
        'Stint',
        'Position',
        'PitInTime',
        'PitOutTime',
        'SpeedI1',
        'SpeedI2',
        'SpeedFL',
        'SpeedST',
        'IsPersonalBest'
    ]]

    # Rename columns
    df.columns = [
        'driver',
        'driver_number',
        'lap',
        'lap_time',
        'sector1',
        'sector2',
        'sector3',
        'tyre',
        'tyre_life',
        'fresh_tyre',
        'stint',
        'position',
        'pit_in',
        'pit_out',
        'speed_i1',
        'speed_i2',
        'speed_fl',
        'speed_st',
        'is_personal_best'
    ]

    return df


# -----------------------------
# 🔁 PROCESS ALL FILES
# -----------------------------
def process_all():
    os.makedirs('data/processed', exist_ok=True)

    for file in os.listdir('data/raw'):
        path = f'data/raw/{file}'

        if 'results' in file:
            df = clean_results(path)
            df.to_csv(f'data/processed/clean_{file}', index=False)

        elif 'laps' in file:
            df = clean_laps(path)
            df.to_csv(f'data/processed/clean_{file}', index=False)

    print("✅ Data cleaned and saved (ADVANCED VERSION)")


# -----------------------------
if __name__ == "__main__":
    process_all()