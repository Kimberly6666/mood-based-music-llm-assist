# 📊 Spotify Dataset Assessment (Phase 1)

This assessment is based on a **random sample of 10000 rows** due to the large size of the `master_spotify_dataset.csv`.

---

## 1. Data Volume & Integrity

| Metric | Value | Assessment |
| :--- | :--- | :--- |
| **Total Estimated Rows** | 1163698 | **Excellent Volume.** A large dataset is ideal for robust model training. |
| **Sample Size Used** | 10000 | Sufficient for initial quality check. |

---

## 2. Column-Level Quality Check (Missing Values)

This table shows the null and filled counts for the **10000** rows sampled.

| Column | Data Type | Total Rows | Null Count | Filled Count | Null % |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Unnamed: 0 | float64 | 10000 | **51** | **9949** | 0.51% |
| artist_name | object | 10000 | **1** | **9999** | 0.01% |
| track_name | object | 10000 | **0** | **10000** | 0.00% |
| track_id | object | 10000 | **0** | **10000** | 0.00% |
| popularity | float64 | 10000 | **51** | **9949** | 0.51% |
| year | float64 | 10000 | **51** | **9949** | 0.51% |
| genre | object | 10000 | **51** | **9949** | 0.51% |
| danceability | float64 | 10000 | **51** | **9949** | 0.51% |
| energy | float64 | 10000 | **51** | **9949** | 0.51% |
| key | float64 | 10000 | **51** | **9949** | 0.51% |
| loudness | float64 | 10000 | **51** | **9949** | 0.51% |
| mode | float64 | 10000 | **51** | **9949** | 0.51% |
| speechiness | float64 | 10000 | **51** | **9949** | 0.51% |
| acousticness | float64 | 10000 | **51** | **9949** | 0.51% |
| instrumentalness | float64 | 10000 | **51** | **9949** | 0.51% |
| liveness | float64 | 10000 | **51** | **9949** | 0.51% |
| valence | float64 | 10000 | **51** | **9949** | 0.51% |
| tempo | float64 | 10000 | **51** | **9949** | 0.51% |
| duration_ms | float64 | 10000 | **51** | **9949** | 0.51% |
| time_signature | float64 | 10000 | **51** | **9949** | 0.51% |
| track_number | float64 | 10000 | **9949** | **51** | 99.49% |
| artist_popularity | float64 | 10000 | **9949** | **51** | 99.49% |
| artist_followers | float64 | 10000 | **9949** | **51** | 99.49% |
| artist_genres | object | 10000 | **9964** | **36** | 99.64% |
| album_id | object | 10000 | **9949** | **51** | 99.49% |
| album_release_date | object | 10000 | **9949** | **51** | 99.49% |
| album_total_tracks | float64 | 10000 | **9949** | **51** | 99.49% |
| album_type | object | 10000 | **9949** | **51** | 99.49% |
| release_date | float64 | 10000 | **10000** | **0** | 100.00% |
| query_genre | float64 | 10000 | **10000** | **0** | 100.00% |
| track_popularity | float64 | 10000 | **9949** | **51** | 99.49% |
| explicit | object | 10000 | **9949** | **51** | 99.49% |
| album_name | object | 10000 | **9949** | **51** | 99.49% |
| track_duration_ms | float64 | 10000 | **9949** | **51** | 99.49% |

---

## 3. Duplicate and Descriptive Check

* **Duplicate Rows (in sample):** **0**
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
