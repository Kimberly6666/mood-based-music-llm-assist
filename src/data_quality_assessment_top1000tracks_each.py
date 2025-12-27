import pandas as pd
import os

def assess_data_quality(file_path):
    """
    Assesses the quality of the data in the given CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary containing the data quality assessment results.
    """
    if not os.path.exists(file_path):
        return {"error": "File not found."}

    df = pd.read_csv(file_path)

    # Basic information
    info = {
        "file_path": file_path,
        "num_rows": len(df),
        "num_cols": len(df.columns),
        "columns": list(df.columns),
    }

    # Missing values
    missing_values = df.isnull().sum().to_dict()

    # Data types
    data_types = {k: str(v) for k, v in df.dtypes.to_dict().items()}

    # Summary statistics for numerical columns
    summary_stats = df.describe().to_dict()

    return {
        "info": info,
        "missing_values": missing_values,
        "data_types": data_types,
        "summary_stats": summary_stats,
    }

if __name__ == "__main__":
    file_path = 'data/raw/Spotify_Popular_East_Asian_Artists_and_Tracks/Top_1000_tracks/jpop_top1000_tracks.csv'
    quality_assessment = assess_data_quality(file_path)
    
    if "error" in quality_assessment:
        print(quality_assessment["error"])
    else:
        # Generate markdown summary
        summary = f"# Data Quality Assessment Summary for jpop Top 1000 Tracks\n\n"
        summary += f"## File Information\n"
        summary += f"- **File Path:** {quality_assessment['info']['file_path']}\n"
        summary += f"- **Number of Rows:** {quality_assessment['info']['num_rows']}\n"
        summary += f"- **Number of Columns:** {quality_assessment['info']['num_cols']}\n"
        summary += f"- **Columns:** {', '.join(quality_assessment['info']['columns'])}\n\n"

        summary += f"## Missing Values\n"
        for col, count in quality_assessment['missing_values'].items():
            summary += f"- **{col}:** {count}\n"
        summary += "\n"

        summary += f"## Data Types\n"
        for col, dtype in quality_assessment['data_types'].items():
            summary += f"- **{col}:** {dtype}\n"
        summary += "\n"

        summary += f"## Summary Statistics\n"
        # Convert summary stats to a more readable format
        stats_df = pd.DataFrame(quality_assessment['summary_stats'])
        summary += stats_df.to_markdown()
        
        output_path = 'docs/data_quality_summary_phase1_top100tracks_jpop.md'
        with open(output_path, 'w') as f:
            f.write(summary)
            
        print(f"Data quality assessment summary generated at '{output_path}'")