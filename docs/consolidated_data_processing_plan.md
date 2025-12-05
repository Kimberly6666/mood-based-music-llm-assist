# Consolidated Data Processing and Unification Plan

## 1. Objective
The primary goal is to produce a single, high-quality, and deduplicated dataset for a mood-based music recommendation system. This plan consolidates findings from initial data quality assessments and outlines a clear path for merging multiple Spotify datasets, while preserving rich metadata like genre tags and audio features.

## 2. Source Datasets
This plan incorporates three main data sources:

1.  **Base Dataset: 1 Million Tracks (`spotify_data.csv`)**
    *   **Role:** Foundation of the final dataset.
    *   **Key Strength:** Contains essential audio features (e.g., `danceability`, `energy`, `valence`) which are critical for mood analysis.
    *   **Identified Issues:** Contains a redundant initial index column (`Unnamed: 0`).

2.  **Enrichment Dataset 1: Global Music (2009-2025)**
    *   **Files:** `spotify_data_clean.csv`, `track_data_final.csv`
    *   **Role:** Augment the base with more recent tracks and updated metadata.
    *   **Key Strength:** Provides up-to-date popularity scores and additional tracks.
    *   **Identified Issues:** `track_duration_min` needs conversion to milliseconds; lacks audio features.

3.  **Enrichment Dataset 2: Popular East Asian Music**
    *   **Files:** `east_asia_top_artists.csv`, and seven top-1000 track files (e.g., `chinese_top1000_tracks.csv`, `kpop_top1000_tracks.csv`, etc.).
    *   **Role:** Ensure representation of popular East Asian music and add detailed artist information.
    *   **Key Strength:** High-quality, clean, and consistently structured data with valuable genre tags. Provides artist-level data like `followers`.
    *   **Identified Issues:**
        *   Redundant index column (`Unnamed: 0`) in all files.
        *   Inconsistent column names (`song_name` vs. `track_name`).
        *   `genres` column is a string representation of a list and requires parsing.
        *   `release_date` needs to be converted to a datetime object.

## 3. Unified Schema
The final dataset will adhere to the schema of the **1 Million Tracks Dataset** to ensure audio feature completeness. A `source_genre` column will be added to retain the original genre tag from the East Asian datasets.

-   `track_id` (Primary Key)
-   `track_name`
-   `artist_name`
-   `album_name`
-   `release_date`
-   `year`
-   `popularity`
-   `duration_ms`
-   `explicit`
-   `genres` (Standardized format)
-   `source_genre` (e.g., 'k-pop', 'j-pop', 'c-pop')
-   `danceability`
-   `energy`
-   `key`
-   `loudness`
-   `mode`
-   `speechiness`
-   `acousticness`
-   `instrumentalness`
-   `liveness`
-   `valence`
-   `tempo`
-   `artist_followers`
-   `artist_popularity`

## 4. Processing and Merge Strategy

### Step 1: Load and Pre-process East Asian Tracks
-   Load all seven `_top1000_tracks.csv` files.
-   For each file:
    -   Add a `source_genre` column populated with the file's genre (e.g., 'k-pop').
    -   Drop the `Unnamed: 0` column.
    -   Rename `song_name` to `track_name`.
    -   Convert `release_date` to datetime objects.
-   Concatenate all seven dataframes into a single `east_asian_tracks` dataframe.

### Step 2: Load and Pre-process Other Datasets
-   **1M Tracks:** Load `spotify_data.csv`. Drop the `Unnamed: 0` column. This is the `base_df`.
-   **Global Music:**
    -   Load `spotify_data clean.csv`. Convert `track_duration_min` to `duration_ms`.
    -   Load `track_data_final.csv`.
    -   Combine these two, keeping the most complete record per `track_id`.
-   **East Asian Artists:** Load `east_asia_top_artists.csv`. Drop the `Unnamed: 0` column.

### Step 3: Combine and Merge
-   Combine the `base_df`, the processed `Global Music` dataframe, and the `east_asian_tracks` dataframe.
-   **Deduplicate** based on `track_id`, prioritizing the record from the `base_df` if duplicates exist, as it contains the crucial audio features.

### Step 4: Enrich with Artist Data
-   Perform a left-merge of the main dataframe with the `east_asian_top_artists` dataframe on `artist_name`. This will add `artist_followers` and other artist-specific data.

### Step 5: Final Cleaning and Standardization
-   **Handle Missing Audio Features:** For tracks that came from the Global and East Asian datasets, audio feature columns will be null. These will be noted for potential future enrichment via the Spotify API (Phase 2).
-   **Standardize Genres:** Parse the `genres` column (where it exists as a string-list) into a standardized format (e.g., a comma-separated string).
-   **Final Schema Check:** Ensure all columns match the Unified Schema, dropping any unnecessary columns (e.g., `_link` columns).

## 5. Execution Workflow Diagram
```mermaid
graph TD
    subgraph "Step 1: Process East Asian Tracks"
        A[Load 7x Top 1000 Tracks CSVs] --> B{Add source_genre, rename columns, drop index};
        B --> C[Concatenate into single DataFrame];
    end

    subgraph "Step 2: Process Other Datasets"
        D[Load spotify_data.csv] --> E{Drop index};
        F[Load Global Music CSVs] --> G{Standardize columns};
        H[Load east_asia_top_artists.csv] --> I{Drop index};
    end

    subgraph "Step 3 & 4: Merge & Enrich"
        E --> J[Combine Base, Global, and East Asian Tracks];
        G --> J;
        C --> J;
        J --> K{Deduplicate on track_id};
        K --> L[Left-merge with Artist data on artist_name];
    end

    subgraph "Step 5: Finalize"
        L --> M[Handle missing audio features & standardize genres];
        M --> N[Final Unified Dataset];
    end