# Data Quality Summary: Phase 1 Assessment

Assessment based on the head (first 50 rows) of each file to determine structure and quality issues.

## General Observations
*   All files share a consistent schema structure.
*   The first column seems to be a redundant index that needs dropping during loading.
*   The 'genres' column contains strings that look like Python lists and will require specific parsing.
*   The 'top_track_explicit' column contains string representations of booleans ('True'/'False').

## File-Specific Assessment

### chinese_top100_artist.csv

*   **Rows Read (Sample):** 50
*   **Column Structure:** Inconsistent
    *Actual Columns:* ['Unnamed: 0', 'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 'top_track_album', 'top_track_popularity', 'top_track_release_date', 'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link']
*   **Missing Values (Sampled Key Columns):**
    *   `artist_name`: 0 null(s)
    *   `popularity`: 0 null(s)
    *   `followers`: 0 null(s)
*   **Inferred Types (Sample):**
    *   `popularity`: int64
    *   `followers`: int64
*   **Explicit Flag Values:** ['False']

### japanese_top100_artist.csv

*   **Rows Read (Sample):** 50
*   **Column Structure:** Inconsistent
    *Actual Columns:* ['Unnamed: 0', 'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 'top_track_album', 'top_track_popularity', 'top_track_release_date', 'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link']
*   **Missing Values (Sampled Key Columns):**
    *   `artist_name`: 0 null(s)
    *   `popularity`: 0 null(s)
    *   `followers`: 0 null(s)
*   **Inferred Types (Sample):**
    *   `popularity`: int64
    *   `followers`: int64
*   **Explicit Flag Values:** ['False', 'True']

### jdance_top100_artist.csv

*   **Rows Read (Sample):** 50
*   **Column Structure:** Inconsistent
    *Actual Columns:* ['Unnamed: 0', 'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 'top_track_album', 'top_track_popularity', 'top_track_release_date', 'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link']
*   **Missing Values (Sampled Key Columns):**
    *   `artist_name`: 0 null(s)
    *   `popularity`: 0 null(s)
    *   `followers`: 0 null(s)
*   **Inferred Types (Sample):**
    *   `popularity`: int64
    *   `followers`: int64
*   **Explicit Flag Values:** ['False', 'True']

### jidol_top100_artist.csv

*   **Rows Read (Sample):** 50
*   **Column Structure:** Inconsistent
    *Actual Columns:* ['Unnamed: 0', 'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 'top_track_album', 'top_track_popularity', 'top_track_release_date', 'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link']
*   **Missing Values (Sampled Key Columns):**
    *   `artist_name`: 0 null(s)
    *   `popularity`: 0 null(s)
    *   `followers`: 0 null(s)
*   **Inferred Types (Sample):**
    *   `popularity`: int64
    *   `followers`: int64
*   **Explicit Flag Values:** ['False', 'nan']

### jpop_top100_artist.csv

*   **Rows Read (Sample):** 50
*   **Column Structure:** Inconsistent
    *Actual Columns:* ['Unnamed: 0', 'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 'top_track_album', 'top_track_popularity', 'top_track_release_date', 'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link']
*   **Missing Values (Sampled Key Columns):**
    *   `artist_name`: 0 null(s)
    *   `popularity`: 0 null(s)
    *   `followers`: 0 null(s)
*   **Inferred Types (Sample):**
    *   `popularity`: int64
    *   `followers`: int64
*   **Explicit Flag Values:** ['False']

### korean_top100_artist.csv

*   **Rows Read (Sample):** 50
*   **Column Structure:** Inconsistent
    *Actual Columns:* ['Unnamed: 0', 'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 'top_track_album', 'top_track_popularity', 'top_track_release_date', 'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link']
*   **Missing Values (Sampled Key Columns):**
    *   `artist_name`: 0 null(s)
    *   `popularity`: 0 null(s)
    *   `followers`: 0 null(s)
*   **Inferred Types (Sample):**
    *   `popularity`: int64
    *   `followers`: int64
*   **Explicit Flag Values:** ['True', 'False']

### kpop_top100_artist.csv

*   **Rows Read (Sample):** 50
*   **Column Structure:** Inconsistent
    *Actual Columns:* ['Unnamed: 0', 'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 'top_track_album', 'top_track_popularity', 'top_track_release_date', 'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link']
*   **Missing Values (Sampled Key Columns):**
    *   `artist_name`: 0 null(s)
    *   `popularity`: 0 null(s)
    *   `followers`: 0 null(s)
*   **Inferred Types (Sample):**
    *   `popularity`: int64
    *   `followers`: int64
*   **Explicit Flag Values:** ['False', 'True']

