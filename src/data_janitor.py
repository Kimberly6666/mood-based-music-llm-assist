import pandas as pd
import pathlib

# 1. Setup Base Directory
# This identifies the 'root dir' based on the script's location in 'src'
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

def prune_spotify_dataset(input_path, output_path, threshold=0.5):
    """
    Cleans a dataset by removing columns with high null counts.
    """
    print(f"Reading data from: {input_path}")
    
    if not input_path.exists():
        print(f"Error: Could not find file at {input_path}")
        return

    # Load dataset
    df = pd.read_csv(input_path)
    
    # Calculate null percentage as identified in the Quality Report
    null_percentage = df.isnull().mean()
    
    # Identify columns to drop (e.g., release_date at 100% or artist_genres at 99.64%)
    cols_to_drop = null_percentage[null_percentage > threshold].index.tolist()
    
    # Execution
    df_cleaned = df.drop(columns=cols_to_drop)
    
    # Persistence
    df_cleaned.to_csv(output_path, index=False)
    
    print(f"--- Processing Complete ---")
    print(f"Columns dropped: {cols_to_drop}")
    print(f"Cleaned file saved to: {output_path}")
    print(f"Final Column Count: {len(df_cleaned.columns)}")

if __name__ == "__main__":
    # Define paths relative to the root directory
    # Structure: root dir -> src -> data -> processed -> file
    source_file = BASE_DIR / "data" / "processed" / "master_spotify_dataset.csv"
    target_file = BASE_DIR / "data" / "processed" / "cleaned_master_spotify_dataset.csv"

    # Call the janitor function with the defined paths
    prune_spotify_dataset(
        input_path=source_file, 
        output_path=target_file, 
        threshold=0.5
    )