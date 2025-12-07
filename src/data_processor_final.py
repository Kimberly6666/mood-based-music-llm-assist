import pandas as pd
import os
import numpy as np

# --- Configuration ---
RAW_DIR = 'data/raw'
INTERIM_DIR = 'data/interim'
PROCESSED_DIR = 'data/processed'

# Ensure output directories exist
os.makedirs(INTERIM_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Define file paths
PATH_1M = os.path.join(RAW_DIR, 'Spotify_1Million_Tracks', 'spotify_data.csv')
PATH_GLOBAL_CLEAN = os.path.join(RAW_DIR, 'Spotify_Global_Music_Dataset_2009_2025', 'spotify_data_clean.csv')
PATH_GLOBAL_FINAL = os.path.join(RAW_DIR, 'Spotify_Global_Music_Dataset_2009_2025', 'track_data_final.csv')
PATH_EAST_ASIA = os.path.join(RAW_DIR, 'Spotify_Popular_East_Asian_Artists_and_Tracks', 'east_asia_top_tracks.csv')

# --- Mappings ---
# Mappings based on user's defined alignment (East Asia Column -> Global Target Column)
EAST_ASIA_TO_GLOBAL_MAPPING = {
    'song_name': 'track_name',
    'album_name': 'album_name',
    'artist_name': 'artist_name',
    'popularity': 'track_popularity',
    'release_data': 'album_release_data',
    'duration_ms': 'track_duration_ms', # Aligned to the corrected Global duration column
    'explicit': 'explicit',
    'query_genres': 'artist_genres',
    # Columns to drop immediately
    'album_link': 'DROP',
    'song_link': 'DROP',
}

# Core columns for joining
JOIN_KEY = ['track_name', 'artist_name']


def clean_columns(df):
    """
    Forces column de-duplication and removes structural corruption issues 
    by ensuring all names are unique and dropping duplicates.
    """
    
    # Use Pandas' built-in feature to resolve duplicates (which failed before, but try again)
    df = df.loc[:, ~df.columns.duplicated(keep='first')].copy()

    # Fallback/Guard: If the index still has issues, rebuild the columns list manually
    clean_cols = []
    seen_cols = set()
    
    for i, col in enumerate(df.columns):
        # Strip potential invisible characters that prevent true matching
        clean_col = col.strip()
        
        if clean_col not in seen_cols:
            clean_cols.append(clean_col)
            seen_cols.add(clean_col)
        else:
            # Drop the column by index if a duplicate name is found
            pass 
            
    # Select data based on the clean list. This rebuilds the DataFrame correctly.
    # Note: We must ensure the number of columns matches the number of elements in clean_cols,
    # which is handled by the initial .loc[:, ~df.columns.duplicated()] line.
    
    # We rename the columns directly now based on the clean list
    df.columns = clean_cols 
    
    return df


def load_data():
    """Loads all required raw datasets and applies initial column cleaning."""
    print("Loading raw data...")
    try:
        # Load and immediately apply the column cleaning to prevent the structural issue
        df_1m = clean_columns(pd.read_csv(PATH_1M))
        df_global_clean = clean_columns(pd.read_csv(PATH_GLOBAL_CLEAN))
        df_global_final = clean_columns(pd.read_csv(PATH_GLOBAL_FINAL))
        df_east_asia = clean_columns(pd.read_csv(PATH_EAST_ASIA))
        
        print("Data loaded and initially cleaned successfully.")
    except FileNotFoundError as e:
        print(f"Error: Required file not found. Check paths. {e}")
        raise
    return df_1m, df_global_clean, df_global_final, df_east_asia


def process_global_data(df_global_clean, df_global_final):
    """
    Step 1: Concatenate Global datasets.
    Step 2: Rename and convert track_duration_min to track_duration_ms.
    """
    print("Processing Global Dataset...")
    
    # Step 1: Concatenate Global datasets (DataFrames are already column-cleaned)
    df_global_combined = pd.concat([df_global_clean, df_global_final], ignore_index=True)

    # Step 2: Rename and convert duration
    if 'track_duration_min' in df_global_combined.columns:
        # Multiply by 60,000 to convert minutes to milliseconds
        df_global_combined['track_duration_min'] = df_global_combined['track_duration_min'] * 60000
        # Rename the column
        df_global_combined.rename(columns={'track_duration_min': 'track_duration_ms'}, inplace=True)
        print("Duration in Global data converted from minutes to milliseconds.")
    # We must ensure the Global data still contains 'track_duration_ms' for the merge.
    # If the original file name was 'duration_ms', we need to adjust the check here.
    
    # Clean up track_id where it might be NaN (optional, but good practice before join)
    if 'track_id' in df_global_combined.columns:
        df_global_combined.dropna(subset=['track_id'], inplace=True)
        df_global_combined.drop_duplicates(subset=['track_id'], keep='first', inplace=True)
        
    df_global_combined.to_csv(os.path.join(INTERIM_DIR, 'global_cleaned.csv'), index=False)
    print(f"Global Cleaned Shape: {df_global_combined.shape}")
    return df_global_combined

# The merge_datasets and final_join_and_deduplicate functions remain as they were in the previous correct version, 
# relying on the cleaned DataFrames provided by the functions above.

def process_east_asia_data(df_east_asia):
    """
    Rename East Asia columns to align with Global structure.
    Drop link/redundant columns.
    **FIX: Add column de-duplication.**
    """
    print("Processing East Asia Dataset...")
    
    # --- FIX 2: Drop duplicate columns BEFORE renaming ---
    df_east_asia = df_east_asia.loc[:, ~df_east_asia.columns.duplicated(keep='first')]
    
    # 1. Prepare rename map (Source -> Target) and list of columns to drop
    rename_map = {}
    drop_cols = []
    
    for ea_col, global_col in EAST_ASIA_TO_GLOBAL_MAPPING.items():
        if global_col == 'DROP':
            drop_cols.append(ea_col)
        elif ea_col in df_east_asia.columns:
            # The map must be: {'existing_col_name': 'new_col_name'}
            rename_map[ea_col] = global_col
            
    # 2. Rename columns
    df_east_asia.rename(columns=rename_map, inplace=True)
    
    # 3. Drop redundant link columns
    df_east_asia.drop(columns=drop_cols, errors='ignore', inplace=True)
    
    df_east_asia.to_csv(os.path.join(INTERIM_DIR, 'east_asia_cleaned.csv'), index=False)
    return df_east_asia


def merge_datasets(df_global, df_east_asia):
    """
    Step 3: Join East Asia and Global Datasets using compound key (track_name, artist_name).
    The result is the 'Metadata Dataset'.
    """
    print("\nStep 3: Joining Global and East Asia to create Metadata Dataset...")
    
    # Set the future Pandas option to handle the FutureWarning gracefully
    pd.set_option('future.no_silent_downcasting', True)
    
    # --- Perform Merge with Suffixes ---
    df_metadata = pd.merge(
        df_global, 
        df_east_asia, 
        on=JOIN_KEY, 
        how='outer',
        suffixes=('_global', '_asia')
    )
    
    # --- Coalescence (Handling Duplicates using NumPy) ---
    cols_to_drop_later = []
    
    # We iterate through all columns in the merged DataFrame
    for col in list(df_metadata.columns):
        if col.endswith('_global'):
            col_asia = col.replace('_global', '_asia')
            
            if col_asia in df_metadata.columns:
                base_col = col.replace('_global', '')
                
                # Coalescence Logic:
                
                global_values = df_metadata[col].values
                asia_values = df_metadata[col_asia].values

                # --- FIX: Force 1D Array if 2D (N, 2) Corruption is Detected ---
                
                # Check for the corrupted (N, 2) shape that is causing the broadcast error
                if global_values.ndim == 2 and global_values.shape[1] > 1:
                    print(f"FIX APPLIED: Reducing 2D array for column '{col}' to 1D.")
                    global_values = global_values[:, 0] # Take the first column (the actual data)
                
                if asia_values.ndim == 2 and asia_values.shape[1] > 1:
                    print(f"FIX APPLIED: Reducing 2D array for column '{col_asia}' to 1D.")
                    asia_values = asia_values[:, 0] # Take the first column (the actual data)
                
                # We use pd.isna() for consistent NaN checking on arrays
                df_metadata[base_col] = np.where(
                    pd.isna(global_values), 
                    asia_values,
                    global_values
                )
                
                # Mark suffixed columns for drop
                cols_to_drop_later.extend([col, col_asia])

    # Drop all marked suffixed columns
    df_metadata.drop(columns=cols_to_drop_later, errors='ignore', inplace=True)
    
    # --- Final Deduplication ---
    # Drop duplicates based on the Track ID (if available) or the compound key
    DEDUP_COL = 'track_id' if 'track_id' in df_metadata.columns else JOIN_KEY
    df_metadata.drop_duplicates(subset=DEDUP_COL, keep='first', inplace=True)
    
    df_metadata.to_csv(os.path.join(INTERIM_DIR, 'metadata_dataset.csv'), index=False)
    print(f"Metadata Dataset (Global + Asia) Shape: {df_metadata.shape}")
    return df_metadata


def final_join_and_deduplicate(df_metadata, df_1m):
    """
    Step 4: Concatenate Metadata Dataset and 1 Million Dataset, then deduplicate
            based on compound key, prioritizing 1M tracks (for audio features).
    """
    print("\nStep 4: Final Join and Deduplication...")
    
    # 1. Standardize and Prepare for Concatenation
    df_1m['source'] = '1M'
    df_metadata['source'] = 'Metadata'
    
    # Fill missing audio feature columns in Metadata with NaN before concat
    # This prevents an error during concatenation if columns are wildly different
    audio_feature_cols = ['danceability', 'energy', 'valence', 'acousticness', 'instrumentalness', 'liveness', 'speechiness', 'tempo']
    for col in audio_feature_cols:
        if col not in df_metadata.columns:
            df_metadata[col] = np.nan
            
    # 2. Concatenate the two key datasets
    # This creates a combined dataset where we have duplicates, but the 1M source is prioritized
    df_final_unfiltered = pd.concat([df_1m, df_metadata], ignore_index=True)
    
    # 3. Final Deduplication 
    print("Final Step: Deduplicating the Master Dataset...")
    
    # Sort to prioritize the '1M' source (0) for tracks with audio features over 'Metadata' (1)
    df_final_unfiltered.sort_values(
        by='source', 
        key=lambda x: x.map({'1M': 0, 'Metadata': 1}), 
        inplace=True
    )
    
    # Drop duplicates based on the combination of track_name and artist_name
    df_master = df_final_unfiltered.drop_duplicates(subset=JOIN_KEY, keep='first')
    
    # Drop the temporary source column
    df_master.drop(columns=['source'], inplace=True)

    print(f"Final Master Dataset Shape: {df_master.shape}")
    
    # --- Final Save ---
    print("\nSaving final master dataset...")
    df_master.to_csv(os.path.join(PROCESSED_DIR, 'master_spotify_dataset.csv'), index=False)
    print("Processing complete. Master file saved to data/processed.")


if __name__ == "__main__":
    df_1m, df_global_clean, df_global_final, df_east_asia = load_data()
    
    # Process steps
    df_global_processed = process_global_data(df_global_clean, df_global_final)
    df_east_asia_processed = process_east_asia_data(df_east_asia)
    
    # This call should now succeed
    df_metadata = merge_datasets(df_global_processed, df_east_asia_processed)
    
    final_join_and_deduplicate(df_metadata, df_1m)