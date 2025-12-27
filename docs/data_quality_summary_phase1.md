# Phase 1 Data Quality Assessment Summary
Date Generated: 2025-12-02 22:51:55

This report assesses data samples obtained using the Unix `head` command due to the large size of the datasets.
**Conclusion for Phase 1:** Review the structural checks and column presence. If samples look correct and headers match expectations, we may proceed. If critical columns are missing or parsing fails repeatedly, further data acquisition or cleaning is required.

## Dataset: Global Music Dataset (2009-2025)
### File: spotify_data clean.csv
---
### Sampled Data (First 5 Lines with Header)
```csv
track_id,track_name,track_number,track_popularity,explicit,artist_name,artist_popularity,artist_followers,artist_genres,album_id,album_name,album_release_date,album_total_tracks,album_type,track_duration_min
3EJS5LyekDim1Tf5rBFmZl,"Trippy Mane (ft. Project Pat)",4,0,TRUE,Diplo,77,2812821,moombahton,5QRFnGnBeMGePBKF2xTz5z,"d00mscrvll, Vol. 1",2025-10-31,9,album,1.55
1oQW6G2ZiwMuHqlPpP27DB,OMG!,1,0,TRUE,Yelawolf,64,2363438,"country hip hop, southern hip hop",4SUmmwnv0xTjRcLdjczGg2,OMG!,2025-10-31,1,single,3.07
7mdkjzoIYlf1rx9EtBpGmU,"Hard 2 Find",1,4,TRUE,"Riff Raff",48,193302,N/A,3E3zEAL8gUYWaLYB9L7gbp,"Hard 2 Find",2025-10-31,1,single,2.55
67rW0Zl7oB3qEpD5YWWE5w,"Still Get Like That (ft. Project Pat & Starrah)",8,30,TRUE,Diplo,77,2813710,moombahton,5QRFnGnBeMGePBKF2xTz5z,"d00mscrvll, Vol. 1",2025-10-31,9,album,1.69
```
### Structural Quality Checks on Sample
*   **Columns Detected:** 15
*   **Sample Rows Parsed:** 4
*   **Columns:** track_id, track_name, track_number, track_popularity, explicit, artist_name, artist_popularity, artist_followers, artist_genres, album_id, album_name, album_release_date, album_total_tracks, album_type, track_duration_min
*   **Columns with No Nulls in Sample:** 14/15
---
### File: track_data_final.csv
---
### Sampled Data (First 5 Lines with Header)
```csv
track_id,track_name,track_number,track_popularity,track_duration_ms,explicit,artist_name,artist_popularity,artist_followers,artist_genres,album_id,album_name,album_release_date,album_total_tracks,album_type
6pymOcrCnMuCWdgGVTvUgP,3,57,61,213173,False,Britney Spears,80.0,17755451.0,['pop'],325wcm5wMnlfjmKZ8PXIIn,The Singles Collection,2009-11-09,58,compilation
2lWc1iJlz2NVcStV5fbtPG,Clouds,1,67,158760,False,BUNT.,69.0,293734.0,['stutter house'],2ArRQNLxf9t0O0gvmG5Vsj,Clouds,2023-01-13,1,single
1msEuwSBneBKpVCZQcFTsU,Forever & Always (Taylor’s Version),11,63,225328,False,Taylor Swift,100.0,145396321.0,[],4hDok0OAJd57SGIT8xuWJH,Fearless (Taylor's Version),2021-04-09,26,album
7bcy34fBT2ap1L4bfPsl9q,I Didn't Change My Number,2,72,158463,True,Billie Eilish,90.0,118692183.0,[],0JGOiO34nwfUdDrD612dOp,Happier Than Ever,2021-07-30,16,album
```
### Structural Quality Checks on Sample
*   **Columns Detected:** 15
*   **Sample Rows Parsed:** 4
*   **Columns:** track_id, track_name, track_number, track_popularity, track_duration_ms, explicit, artist_name, artist_popularity, artist_followers, artist_genres, album_id, album_name, album_release_date, album_total_tracks, album_type
*   **Columns with No Nulls in Sample:** 15/15
---

## Dataset: Popular East Asian Artists and Tracks
### File: east_asia_top_artists.csv
---
### Sampled Data (First 5 Lines with Header)
```csv
,artist_name,popularity,followers,artist_link,genres,top_track,top_track_album,top_track_popularity,top_track_release_date,top_track_duration_ms,top_track_explicit,top_track_album_link,top_track_link,query_genre
0,BTS,88,67507448,https://open.spotify.com/artist/3Nrfpe0tUJi4K4DXYWgMUX,"['k-pop', 'k-pop boy group', 'pop']",Left and Right (Feat. Jung Kook of BTS),CHARLIE,88.0,2022-10-06,154486.0,False,https://open.spotify.com/album/5Jk4Eg7pxYhDrWJCVVzmMt,https://open.spotify.com/track/5Odq8ohlgIbQKMZivbWkEo,j-pop
1,BLACKPINK,82,43385244,https://open.spotify.com/artist/41MozSoPIsD1dJM0CLPjZF,"['k-pop', 'k-pop girl group', 'pop']",Shut Down,BORN PINK,79.0,2022-09-15,175889.0,False,https://open.spotify.com/album/0kbZ4ZNRs76sSFeGUEErFM,https://open.spotify.com/track/7gRFDGEzF9UkBV233yv2dc,j-pop
2,TWICE,79,18278225,https://open.spotify.com/artist/7n2Ycct7Beij7Dj7meI4X0,"['k-pop', 'k-pop girl group', 'pop']",MOONLIGHT SUNRISE,READY TO BE,75.0,2023-03-10,180320.0,False,https://open.spotify.com/album/7hzP5i7StxYG4StECA0rrJ,https://open.spotify.com/track/5IN9W6eUfk3014My9awagX,j-pop
3,j-hope,70,15407840,https://open.spotify.com/artist/0b1sIQumIAsNbqAoIClSpy,"['k-pop', 'k-rap']",on the street (with J. Cole),on the street (with J. Cole),83.0,2023-03-03,214701.0,True,https://open.spotify.com/album/70xdtgH5XuYTqBNdNbUwGO,https://open.spotify.com/track/5wxYxygyHpbgv0EXZuqb9V,j-pop
```
### Structural Quality Checks on Sample
*   **Columns Detected:** 15
*   **Sample Rows Parsed:** 4
*   **Columns:** Unnamed: 0, artist_name, popularity, followers, artist_link, genres, top_track, top_track_album, top_track_popularity, top_track_release_date, top_track_duration_ms, top_track_explicit, top_track_album_link, top_track_link, query_genre
*   **Columns with No Nulls in Sample:** 15/15
---
### File: east_asia_top_tracks.csv
---
### Sampled Data (First 5 Lines with Header)
```csv
,song_name,album_name,album_link,artist_name,popularity,release_date,song_link,duration_ms,explicit,query_genre
0,Cupid - Twin Ver.,The Beginning: Cupid,https://open.spotify.com/album/5letLUZIFsQikJYShfGNs4,FIFTY FIFTY,98,2023-02-24,https://open.spotify.com/track/7FbrGaHYVDmfr7KoLIZnQ7,174253,False,k-pop
1,Seven (feat. Latto) (Explicit Ver.),Seven (feat. Latto),https://open.spotify.com/album/53985D8g3JcGBoULSOYYKX,Jung Kook,97,2023-07-14,https://open.spotify.com/track/7x9aauaA9cu6tyfpHnqDLo,184400,True,k-pop
2,Like Crazy,FACE,https://open.spotify.com/album/4xc3Lc9yASZgEJGH7acWMB,Jimin,96,2023-03-24,https://open.spotify.com/track/3Ua0m0YmEjrMi9XErKcNiR,212241,False,k-pop
3,MONEY,LALISA,https://open.spotify.com/album/4ASxFYWyk2216OloHoaSh8,LISA,96,2021-09-10,https://open.spotify.com/track/45OX2jjEw1l7lOFJfDP9fv,168227,False,k-pop
```
### Structural Quality Checks on Sample
*   **Columns Detected:** 11
*   **Sample Rows Parsed:** 4
*   **Columns:** Unnamed: 0, song_name, album_name, album_link, artist_name, popularity, release_date, song_link, duration_ms, explicit, query_genre
*   **Columns with No Nulls in Sample:** 11/11
---

## Dataset: 1 Million Tracks Dataset
### File: spotify_data.csv
---
### Sampled Data (First 5 Lines with Header)
```csv
,artist_name,track_name,track_id,popularity,year,genre,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature
0,Jason Mraz,I Won't Give Up,53QF56cjZA9RTuuMZDrSA6,68,2012,acoustic,0.483,0.303,4,-10.058,1,0.0429,0.694,0.0,0.115,0.139,133.406,240166,3
1,Jason Mraz,93 Million Miles,1s8tP3jP4GZcyHDsjvw218,50,2012,acoustic,0.572,0.454,3,-10.286,1,0.0258,0.477,1.37e-05,0.0974,0.515,140.182,216387,4
2,Joshua Hyslop,Do Not Let Me Go,7BRCa8MPiyuvr2VU3O9W0F,57,2012,acoustic,0.409,0.234,3,-13.711,1,0.0323,0.338,5e-05,0.0895,0.145,139.832,158960,4
3,Boyce Avenue,Fast Car,63wsZUhUZLlh1OsyrZq7sz,58,2012,acoustic,0.392,0.251,10,-9.845,1,0.0363,0.807,0.0,0.0797,0.508,204.961,304293,4
```
### Structural Quality Checks on Sample
*   **Columns Detected:** 20
*   **Sample Rows Parsed:** 4
*   **Columns:** Unnamed: 0, artist_name, track_name, track_id, popularity, year, genre, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature
*   **Columns with No Nulls in Sample:** 20/20
---
