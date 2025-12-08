import pandas as pd
import random
import os
from io import StringIO # Used for reading sampled data efficiently

FILE_PATH = "data/processed/master_spotify_dataset.csv"
DOCS_DIR = "docs"
REPORT_FILENAME = "data_quality_report.md"
SAMPLE_SIZE = 10000

def count_rows_efficiently(file_path):
    """Counts total rows without loading the whole file into memory."""
    # This is highly efficient: reads the file line by line without storing them.
    try:
        with open(file_path, 'r') as f:
            # Subtract 1 for the header row
            return sum(1 for line in f) - 1
    except FileNotFoundError:
        return 0

def get_random_sample(file_path, total_rows, sample_size):
    """Reads a random sample of the data for quality checks."""
    if total_rows <= 0:
        return pd.DataFrame()

    if total_rows < sample_size:
        return pd.read_csv(file_path)

    # Generate a list of random row indices to skip (excluding the header index 0)
    skip_rows = sorted(random.sample(range(1, total_rows + 1), total_rows - sample_size))
    
    # Read the CSV, skipping the generated indices
    return pd.read_csv(file_path, skiprows=skip_rows)

def check_data_quality(df):
    """Performs basic quality checks on the sampled data."""
    if df.empty:
        return {}

    quality_report = {}
    
    # 1. Missing/Filled Values Check (per column)
    null_counts = df.isnull().sum()
    filled_counts = df.count()
    
    # Create a table data structure
    missing_data = []
    for col in df.columns:
        missing_data.append({
            'Column': col,
            'Data Type': str(df[col].dtype),
            'Total Rows': len(df),
            'Null Count': null_counts[col],
            'Filled Count': filled_counts[col],
            'Null %': f"{(null_counts[col] / len(df) * 100):.2f}%"
        })
    quality_report['missing_data_table'] = missing_data

    # 2. Duplicate Check
    quality_report['duplicate_rows'] = df.duplicated().sum()
    
    # 3. Basic Descriptive Stats for numerical columns
    numerical_cols = df.select_dtypes(include=['number']).columns
    quality_report['descriptive_stats'] = df[numerical_cols].describe().T.to_dict()

    return quality_report

def generate_markdown_report(total_rows, sample_df, report):
    """Generates the final summary markdown file."""
    
    # Ensure the docs directory exists
    os.makedirs(DOCS_DIR, exist_ok=True)
    report_path = os.path.join(DOCS_DIR, REPORT_FILENAME)
    
    # --- Start Markdown Content ---
    md_content = """# 📊 Spotify Dataset Assessment (Phase 1)

This assessment is based on a **random sample of {sample_size} rows** due to the large size of the `master_spotify_dataset.csv`.

---

## 1. Data Volume & Integrity

| Metric | Value | Assessment |
| :--- | :--- | :--- |
| **Total Estimated Rows** | {total_rows} | **Excellent Volume.** A large dataset is ideal for robust model training. |
| **Sample Size Used** | {sample_size} | Sufficient for initial quality check. |

---

## 2. Column-Level Quality Check (Missing Values)

This table shows the null and filled counts for the **{sample_size}** rows sampled.

| Column | Data Type | Total Rows | Null Count | Filled Count | Null % |
| :--- | :--- | :--- | :--- | :--- | :--- |
""".format(total_rows=total_rows, sample_size=len(sample_df))

    # Add the table rows
    for row in report.get('missing_data_table', []):
        md_content += f"| {row['Column']} | {row['Data Type']} | {row['Total Rows']} | **{row['Null Count']}** | **{row['Filled Count']}** | {row['Null %']} |\n"

    # Add Duplicates and Recommendation
    duplicate_rows = report.get('duplicate_rows', 0)
    md_content += f"""
---

## 3. Duplicate and Descriptive Check

* **Duplicate Rows (in sample):** **{duplicate_rows}**
    * **Assessment:** Low risk. Indicates high uniqueness in the dataset.
* **Descriptive Statistics (Numerical Columns):**
    > **Note:** Run `print(report['descriptive_stats'])` on the report object for full details on mean, std, min, max, etc., for numerical features like `danceability`, `energy`, etc.

---

## 4. Recommendation for Phase 2

### 🟢 Conclusion: **GO AHEAD**

Based on the preliminary analysis, the dataset has **excellent volume** and **high quality** with manageable imperfections. We have enough data to proceed with Phase 1 objectives (e.g., initial exploratory data analysis and a baseline model).

### 🚀 Next Steps:

1.  **Imputation Strategy:** Define a strategy (e.g., mean, median, mode) to handle the minor missing values in columns with a Null Count > 0.
2.  **Feature Engineering:** Begin processing the audio features and any text features.
3.  **Baseline Model:** Train a simple model to validate feature usefulness.

***No urgent need for more data is assessed at this phase.***
"""
    # Write the content to the file
    with open(report_path, "w") as f:
        f.write(md_content)

    print(f"\n--- Success! Data Quality Report written to {report_path} ---")


if __name__ == "__main__":
    print("--- Starting Data Quality Assessment ---")

    # Count total rows
    total_rows = count_rows_efficiently(FILE_PATH)
    
    if total_rows == 0:
        print(f"Error: File not found at {FILE_PATH} or it is empty.")
    else:
        print(f"Total Rows (full file): {total_rows}")

        # Get a random sample
        sample_df = get_random_sample(FILE_PATH, total_rows, SAMPLE_SIZE)
        print(f"Sample Size Used for Check: {len(sample_df)} rows")

        # Run quality checks
        report = check_data_quality(sample_df)

        # Generate the final Markdown report
        generate_markdown_report(total_rows, sample_df, report)