# Data Quality Assessment Summary for jdance Top 1000 Tracks

## File Information
- **File Path:** data/raw/Spotify_Popular_East_Asian_Artists_and_Tracks/Top_1000_tracks/jdance_top1000_tracks.csv
- **Number of Rows:** 1000
- **Number of Columns:** 10
- **Columns:** Unnamed: 0, song_name, album_name, album_link, artist_name, popularity, release_date, song_link, duration_ms, explicit

## Missing Values
- **Unnamed: 0:** 0
- **song_name:** 0
- **album_name:** 0
- **album_link:** 0
- **artist_name:** 0
- **popularity:** 0
- **release_date:** 0
- **song_link:** 0
- **duration_ms:** 0
- **explicit:** 0

## Data Types
- **Unnamed: 0:** int64
- **song_name:** object
- **album_name:** object
- **album_link:** object
- **artist_name:** object
- **popularity:** int64
- **release_date:** object
- **song_link:** object
- **duration_ms:** int64
- **explicit:** bool

## Summary Statistics
|       |   Unnamed: 0 |   popularity |   duration_ms |
|:------|-------------:|-------------:|--------------:|
| count |     1000     |    1000      |        1000   |
| mean  |      500.5   |      30.276  |      224829   |
| std   |      288.819 |      11.4504 |       53108.1 |
| min   |        1     |       2      |       32900   |
| 25%   |      250.75  |      22      |      193726   |
| 50%   |      500.5   |      27.5    |      222480   |
| 75%   |      750.25  |      36      |      250400   |
| max   |     1000     |      80      |      510396   |