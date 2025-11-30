# Data Acquisition Plan for Mood-Based Music LLM

This document details the recommended approach for acquiring music data matching the required criteria: Chinese (1980-2025), English (1970-2025), and Korean (2000-2025).

## 1. Strategy Overview
Since direct web browsing is restricted, this plan suggests command-line actions the user should take, focusing on utilizing common open-source data libraries and platforms (Hugging Face, Kaggle).

## 2. English Data Acquisition (1970-2025)
**Primary Targets:** Large-scale lyric/metadata sets.
**Recommended Action (User executes):** If the `huggingface_hub` Python library is installed, search for datasets tagged with 'lyrics', 'music', and year metadata range.

Example search command (User runs in terminal):
`huggingface-cli search --datasets lyrics english 1970..2025` (If CLI is installed)

**Fallback:** Utilize established academic datasets like MSD derivatives, focusing on filtering metadata tables to ensure 1970 start date coverage.

## 3. Chinese Data Acquisition (1980-2025)
**Primary Targets:** Mandopop/C-Pop lyrics and release year data. This is the most challenging due to less standardized English naming conventions.
**Recommended Action (User executes):** Search Kaggle notebooks or Hugging Face for specific "Mandopop" or "C-Pop" datasets.

Example search command (User runs in terminal):
`huggingface-cli search --datasets mandopop`

## 4. Korean Data Acquisition (2000-2025)
**Primary Targets:** K-Pop data, focusing on chart performance and lyrics.
**Recommended Action (User executes):** Search Hugging Face for datasets explicitly mentioning K-Pop and including release years post-2000.

Example search command (User runs in terminal):
`huggingface-cli search --datasets kpop lyrics 2000..2025`

## 5. Next Steps (Post-Acquisition)
Once data is downloaded (e.g., into a `./data/raw/` directory), Todo #3 (Data Ingestion Pipeline) will commence, involving cleaning, normalization, and preparation for vector embedding.