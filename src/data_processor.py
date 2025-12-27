import pandas as pd

def process_data(english_data_path, chinese_data_path, korean_data_path):
    """
    Processes music data from different sources and combines them into a single dataset.

    Args:
        english_data_path (str): Path to the English music data CSV file.
        chinese_data_path (str): Path to the Chinese music data CSV file.
        korean_data_path (str): Path to the Korean music data CSV file.

    Returns:
        pandas.DataFrame: A combined dataset containing music data from all sources.
    """

    # Load the data from the CSV files
    try:
        english_data = pd.read_csv(english_data_path)
    except FileNotFoundError:
        print(f"Error: English data file not found at {english_data_path}")
        english_data = pd.DataFrame()

    try:
        chinese_data = pd.read_csv(chinese_data_path)
    except FileNotFoundError:
        print(f"Error: Chinese data file not found at {chinese_data_path}")
        chinese_data = pd.DataFrame()

    try:
        korean_data = pd.read_csv(korean_data_path)
    except FileNotFoundError:
        print(f"Error: Korean data file not found at {korean_data_path}")
        korean_data = pd.DataFrame()

    # Standardize column names (example: lowercase and replace spaces with underscores)
    def standardize_columns(df):
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        return df

    english_data = standardize_columns(english_data)
    chinese_data = standardize_columns(chinese_data)
    korean_data = standardize_columns(korean_data)

    # Identify common columns
    common_columns = list(set(english_data.columns) & set(chinese_data.columns) & set(korean_data.columns))

    # Select common columns
    english_data = english_data[common_columns]
    chinese_data = chinese_data[common_columns]
    korean_data = korean_data[common_columns]

    # Combine the data
    combined_data = pd.concat([english_data, chinese_data, korean_data], ignore_index=True)

    # Remove duplicates
    combined_data = combined_data.drop_duplicates()

    # Data Cleaning: Remove rows with missing values in key columns
    key_columns = ['artist_name', 'track_name', 'release_year']  # Replace with your actual key columns
    combined_data = combined_data.dropna(subset=key_columns)

    # Feature Selection: Select columns relevant for mood-based recommendation
    relevant_columns = ['artist_name', 'track_name', 'release_year', 'genre', 'lyrics', 'mood']  # Replace with your actual relevant columns
    combined_data = combined_data[relevant_columns]

    # Data Standardization: Standardize genre column
    def standardize_genre(genre):
        if isinstance(genre, str):
            return genre.lower().strip()
        else:
            return ''

    combined_data['genre'] = combined_data['genre'].apply(standardize_genre)

    # Print basic statistics
    print(f"Combined data shape: {combined_data.shape}")
    print(combined_data.head())

    return combined_data


if __name__ == "__main__":
    # Example usage: Replace with the actual paths to your data files
    english_data_path = 'data/raw/Spotify_Global_Music_Dataset_2009_2025/track_data_final.csv'
    chinese_data_path = 'data/raw/Spotify_Popular_East_Asian_Artists_and_Tracks/east_asia_top_artists.csv'
    korean_data_path = 'data/raw/Spotify_Popular_East_Asian_Artists_and_Tracks/east_asia_top_tracks.csv' # contains korean songs

    # Process the data
    music_data = process_data(english_data_path, chinese_data_path, korean_data_path)

    # Save the processed data to a CSV file
    music_data.to_csv('data/processed/music_data.csv', index=False)