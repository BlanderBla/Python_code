import pandas as pd

df = pd.read_csv('Spotify_Song_Attributes.csv')
print(df)
df_sortedArtis = df.sort_values(by='artistName', ascending=True)
print(df_sortedArtis)
df_sortedArtis.to_csv("Spotify_Song_Ordered.csv", index=False)