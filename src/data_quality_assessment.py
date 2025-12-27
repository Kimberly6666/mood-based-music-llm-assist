import pandas as pd
import subprocess
import os

# Define the datasets and their primary files to check
DATASETS = {
    "Global Music Dataset (2009-2025)": [
        {
            "name": "spotify_data clean.csv",
            "path": "data/raw/Spotify_Global_Music_Dataset_2009_2025/spotify_data_clean.csv",
            "sample_lines": 5
        },
        {
            "name": "track_data_final.csv",
            "path": "data/raw/Spotify_Global_Music_Dataset_2009_2025/track_data_final.csv",
            "sample_lines": 5
        },
    ],
    "Popular East Asian Artists and Tracks": [
        {
            "name": "east_asia_top_artists.csv",
            "path": "data/raw/Spotify_Popular_East_Asian_Artists_and_Tracks/east_asia_top_artists.csv",
            "sample_lines": 5
        },
        {
            "name": "east_asia_top_tracks.csv",
            "path": "data/raw/Spotify_Popular_East_Asian_Artists_and_Tracks/east_asia_top_tracks.csv",
            "sample_lines": 5
        },
        # Ignoring subdirectories for top-level assessment, focusing on main summary files
    ],
    "1 Million Tracks Dataset": [
        {
            "name": "spotify_data.csv",
            "path": "data/raw/Spotify_1Million_Tracks/spotify_data.csv",
            "sample_lines": 5
        }
    ]
}

REPORT_PATH = "docs/data_quality_summary_phase1.md"
HEAD_COMMAND = "head -n {lines} {path}"

def run_head_command(file_path, num_lines):
    """Executes 'head' command via subprocess and returns content."""
    command = HEAD_COMMAND.format(lines=num_lines, path=file_path)
    try:
        # Execute the command in the current workspace directory
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True,
            cwd=os.getcwd() # Ensure execution context is correct
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"ERROR: Command failed for {file_path}. Stderr: {e.stderr.strip()}"
    except FileNotFoundError:
        return f"ERROR: 'head' command not found or file not accessible: {file_path}"

def assess_sample(file_path, sample_content):
    """Performs basic data quality assessment on sampled content."""
    report = []
    
    # Check if head command failed
    if sample_content.startswith("ERROR:"):
        report.append(f"**Sampling Error:** {sample_content}")
        return "\n".join(report)

    # 1. Check if the sample is empty (might indicate file is small or command failed silently)
    if not sample_content.strip():
        report.append("**Sampling Warning:** Sample content is empty.")
        return "\n".join(report)
        
    report.append("---")
    report.append("### Sampled Data (First 5 Lines with Header)")
    report.append("```csv")
    report.append(sample_content.strip())
    report.append("```")

    # 2. Attempt to load sample into pandas for structure check (requires at least header + 1 line of data, but we check structure based on CSV parsing)
    try:
        # We use io.StringIO to read the sample content as if it were a file
        from io import StringIO
        df_sample = pd.read_csv(StringIO(sample_content))
        
        report.append("### Structural Quality Checks on Sample")
        report.append(f"*   **Columns Detected:** {len(df_sample.columns)}")
        report.append(f"*   **Sample Rows Parsed:** {len(df_sample)}")
        report.append(f"*   **Columns:** {', '.join(df_sample.columns.tolist())}")
        
        # Basic null check on the sample
        null_counts = df_sample.isnull().sum()
        non_null_cols = null_counts[null_counts == 0]
        
        if not non_null_cols.empty:
            report.append(f"*   **Columns with No Nulls in Sample:** {len(non_null_cols)}/{len(df_sample.columns)}")
        
        # Check for immediate parsing issues (e.g., too many columns indicated by low row count)
        if len(df_sample) < 2 and not df_sample.empty: # Header only, or header + 1 row
             report.append("**Data Integrity Warning:** Only header or very few rows parsed. File might be extremely large or corrupt.")
             
    except Exception as e:
        report.append(f"**Pandas Parsing Error:** Could not fully parse sample into DataFrame. Error: {str(e)}")

    report.append("---")
    return "\n".join(report)


def generate_report():
    """Generates the overall data quality summary report."""
    report_lines = ["# Phase 1 Data Quality Assessment Summary",
                    f"Date Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}",
                    "",
                    "This report assesses data samples obtained using the Unix `head` command due to the large size of the datasets.",
                    "**Conclusion for Phase 1:** Review the structural checks and column presence. If samples look correct and headers match expectations, we may proceed. If critical columns are missing or parsing fails repeatedly, further data acquisition or cleaning is required.",
                    ""]
    
    for dataset_name, files in DATASETS.items():
        report_lines.append(f"## Dataset: {dataset_name}")
        for file_info in files:
            report_lines.append(f"### File: {file_info['name']}")
            
            # 1. Get sample content using shell command
            sample_content = run_head_command(file_info["path"], file_info["sample_lines"])
            
            # 2. Assess sample content
            assessment = assess_sample(file_info["path"], sample_content)
            
            report_lines.append(assessment)
        report_lines.append("")

    # Write report to file
    final_content = "\n".join(report_lines)
    try:
        with open(REPORT_PATH, 'w') as f:
            f.write(final_content)
        return f"Data quality assessment script written to 'src/data_quality_assessment.py'. Report output path: {REPORT_PATH}"
    except Exception as e:
        return f"ERROR: Could not write report file {REPORT_PATH}. {e}"


if __name__ == "__main__":
    # Before running the main logic, we check if pandas is available via an inline check, 
    # although we rely on requirements.txt being processed.
    try:
        import pandas as pd
        print(f"Pandas version: {pd.__version__}")
        print("Starting data assessment...")
        
        # Execute the generation process
        result_message = generate_report()
        print(result_message)
        
    except ImportError:
        print("ERROR: pandas library is required but not installed. Please run 'pip install -r requirements.txt' or specifically 'pip install pandas'.")
    except Exception as e:
        print(f"An unexpected error occurred during script execution: {e}")
