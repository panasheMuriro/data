import pandas as pd

nba_data = pd.read_csv("nba_24_25.csv")
nba_data = nba_data.drop(columns=["RANK"])

team_agg = nba_data.groupby("TEAM").agg({
    "PPG": "mean",  # Average points per game
    "RPG": "mean",  # Average rebounds per game
    "3P%": "mean",  # Average assists per game
    "MPG": "sum",   # Total minutes played
})

# Display the aggregated stats
print(team_agg.head())