import fastf1
import pandas as pd
import os

# create cache folder
os.makedirs('cache', exist_ok=True)

fastf1.Cache.enable_cache('cache')

year = 2026
race = "Australian Grand Prix"

# load race session
session = fastf1.get_session(year, race, 'R')
session.load()

laps = session.laps

df = laps[['Driver','Team','LapNumber','LapTime','Sector1Time','Sector2Time','Sector3Time','Compound','TyreLife','Position']].copy()

# convert times to seconds for Tableau
df['LapTime'] = pd.to_timedelta(df['LapTime']).dt.total_seconds()
df['Sector1Time'] = pd.to_timedelta(df['Sector1Time']).dt.total_seconds()
df['Sector2Time'] = pd.to_timedelta(df['Sector2Time']).dt.total_seconds()
df['Sector3Time'] = pd.to_timedelta(df['Sector3Time']).dt.total_seconds()

# remove rows where lap time is missing
df = df.dropna(subset=['LapTime'])

# save dataset
df.to_csv("melbourne_tableau_dataset.csv", index=False)

print("Dataset ready for Tableau visualization")