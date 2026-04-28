import fastf1

fastf1.Cache.enable_cache('data/cache')

# Load a sample session
session = fastf1.get_session(2025, 'Monaco', 'R')
session.load()

print(session.results.head())