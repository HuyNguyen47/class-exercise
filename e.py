from pathlib import Path
import pandas as pd
data_path = Path("data") / "messy_netflix_titles.csv"
df = pd.read_csv(data_path)

# selected = df[["title", "type"]]
# print(selected.head())
# print(type(selected))

# movies = df[df["type"] == "Movie"]
# print(movies.head())
# print(movies.shape[0])

# result = df.loc[df["release_year"] >= 2020,["title", "type"]]
# print(result.head())

# print(df[df.duplicated()])

# before = len(df)
# df = df.drop_duplicates()
# print(f"Removed {before - len(df)} duplicate row(s)")

movies = df[df["type"] == "Movie"]
print(movies.head())
print(movies.shape)
