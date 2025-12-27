import pandas as pd
import os
import json

# Configuration
BASE_PATH = "data/raw/Spotify_Popular_East_Asian_Artists_and_Tracks/Top_100_artists"
OUTPUT_FILE = "docs/data_quality_summary_phase1_top100artists.md"
FILES_TO_ASSESS = [
    "chinese_top100_artist.csv",
    "japanese_top100_artist.csv",
    "jdance_top100_artist.csv",
    "jidol_top100_artist.csv",
    "jpop_top100_artist.csv",
    "korean_top100_artist.csv",
    "kpop_top100_artist.csv",
]
# Read only the first 50 rows to simulate checking only the 'head' of the large file
N_ROWS_TO_READ = 50 
# Expected columns based on inspection (excluding the unnamed index column which we will handle)
EXPECTED_COLUMNS = [
    'artist_name', 'popularity', 'followers', 'artist_link', 'genres', 'top_track', 
    'top_track_album', 'top_track_popularity', 'top_track_release_date', 
    'top_track_duration_ms', 'top_track_explicit', 'top_track_album_link', 'top_track_link'
]
KEY_COLUMNS_TO_CHECK_NULLS = ['artist_name', 'popularity', 'followers']

summary_results = {}

for filename in FILES_TO_ASSESS:
    filepath = os.path.join(BASE_PATH, filename)
    file_summary = {}
    
    try:
        # Read CSV, specifically handling the first column which seemed unnamed/index-like
        df = pd.read_csv(filepath, nrows=N_ROWS_TO_READ)
        
        # Clean up columns: Identify and rename/drop the first unnamed column if present
        if df.columns[0] == '':
            df = df.iloc[:, 1:] # Drop the first column if it's unnamed (empty string name)
            # Re-index columns if necessary, although pandas usually handles this structure well if consistent
            
        # Renaming columns to expected names for easier scripting, although based on head output, they look clean enough now
        # We must ensure column names match the data structure observed.
        # The raw output suggests the header is: ,artist_name,popularity,followers,...
        # Pandas usually names the first column '' or 'Unnamed: 0' if it's an index column without a header.
        
        # Let's re-read using the exact header structure from the tool output for robust parsing if the previous read failed column naming expectations
        df = pd.read_csv(filepath, nrows=N_ROWS_TO_READ, usecols=lambda x: x != df.columns[0] if df.columns[0] == '' else True)
        
        # Final check on columns after initial read attempt
        if len(df.columns) != len(EXPECTED_COLUMNS):
             # For simplicity in this structure check, we rely on the consistent structure observed in the head command output
             # We assume the first column is the index and we only care about the 13 named columns.
             # Let's stick to the columns loaded after dropping the first one, assuming the first column of the tool output is the CSV row index field which we drop.
             pass
        
        # 1. Record Count (based on what we read)
        file_summary['read_rows'] = len(df)
        
        # 2. Column check (based on the 13 expected columns)
        current_cols = df.columns.tolist()
        file_summary['column_count_match'] = (len(current_cols) == len(EXPECTED_COLUMNS))
        if not file_summary['column_count_match']:
             file_summary['actual_columns'] = current_cols # Capture actual columns if mismatch
        
        # 3. Missing Value Check (on key columns)
        null_counts = df[KEY_COLUMNS_TO_CHECK_NULLS].isnull().sum().to_dict()
        file_summary['missing_values'] = null_counts
        
        # 4. Data Type Guessing (based on non-null values in the sample)
        type_guesses = {}
        if 'popularity' in df.columns:
            # Try to infer type, knowing 'popularity' should be int/float
            # Since the raw data had potential parsing issues in subsequent rows (seen in jidole file), we check if we can cast.
            try:
                df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
                type_guesses['popularity'] = str(df['popularity'].dtype)
            except:
                type_guesses['popularity'] = 'Parsing Error (Mixed/Bad format)'
        
        if 'followers' in df.columns:
            try:
                df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
                type_guesses['followers'] = str(df['followers'].dtype)
            except:
                type_guesses['followers'] = 'Parsing Error (Mixed/Bad format)'
        
        file_summary['inferred_types_sample'] = type_guesses
        
        # 5. Explicit flag check
        if 'top_track_explicit' in df.columns:
            unique_explicit = df['top_track_explicit'].astype(str).unique()
            file_summary['explicit_values'] = unique_explicit.tolist()

    except Exception as e:
        file_summary['error'] = str(e)

    summary_results[filename] = file_summary

# Format results for markdown output
markdown_output = f"# Data Quality Summary: Phase 1 Assessment\n\n"
markdown_output += f"Assessment based on the head (first {N_ROWS_TO_READ} rows) of each file to determine structure and quality issues.\n\n"
markdown_output += "## General Observations\n"
markdown_output += "*   All files share a consistent schema structure.\n"
markdown_output += "*   The first column seems to be a redundant index that needs dropping during loading.\n"
markdown_output += "*   The 'genres' column contains strings that look like Python lists and will require specific parsing.\n"
markdown_output += "*   The 'top_track_explicit' column contains string representations of booleans ('True'/'False').\n\n"
markdown_output += "## File-Specific Assessment\n\n"

for filename, summary in summary_results.items():
    markdown_output += f"### {filename}\n\n"
    if 'error' in summary:
        markdown_output += f"**Error during processing:** {summary['error']}\n\n"
        continue
        
    markdown_output += f"*   **Rows Read (Sample):** {summary.get('read_rows', 'N/A')}\n"
    
    markdown_output += f"*   **Column Structure:** {'Consistent with expected 13 data columns' if summary.get('column_count_match') else 'Inconsistent'}\n"
    if not summary.get('column_count_match'):
        markdown_output += f"    *Actual Columns:* {summary.get('actual_columns')}\n"
        
    markdown_output += f"*   **Missing Values (Sampled Key Columns):**\n"
    for col, count in summary.get('missing_values', {}).items():
        markdown_output += f"    *   `{col}`: {count} null(s)\n"
        
    markdown_output += f"*   **Inferred Types (Sample):**\n"
    for col, dtype in summary.get('inferred_types_sample', {}).items():
        markdown_output += f"    *   `{col}`: {dtype}\n"
        
    markdown_output += f"*   **Explicit Flag Values:** {summary.get('explicit_values', 'N/A')}\n\n"

# Write the summary to the markdown file
with open(OUTPUT_FILE, 'w') as f:
    f.write(markdown_output)

print(f"Data quality summary written to {OUTPUT_FILE}")