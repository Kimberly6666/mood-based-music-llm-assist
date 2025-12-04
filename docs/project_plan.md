# Semantic Playlist Generator and Music Discovery Chatbot Plan

## 1. Product Vision & Goals
To develop an advanced music recommendation system leveraging LLMs to interpret natural language queries (moods, musical characteristics) and provide nuanced playlists and explanations, catering to casual listeners, enthusiasts, and professionals.

## 2. Required Data Sources (Initial Recommendations)
The LLM requires rich data for training/RAG: lyrics, metadata (artist, genre, year), and potentially qualitative data (reviews/interviews).

| Language | Time Range | Focus Areas | Potential Sources (To be confirmed/downloaded) |
| :--- | :--- | :--- | :--- |
| English | 1970-2025 | Comprehensive catalog, genre diversity | Lakh MIDI Dataset derivatives, large public lyric corpora (e.g., Genius/AZLyrics scrapes), MusicBrainz metadata. |
| Chinese | 1980-2025 | Mandopop, C-Pop hits | Academic Chinese music corpora, specialized GitHub repositories, Kaggle datasets related to C-Pop lyrics/charts. |
| Korean | 2000-2025 | K-Pop, ballad, rock subsets | K-Pop specific datasets, chart archives (Melon/Gaon equivalents if available publicly), Korean lyric databases. |

*Note: Data acquisition must comply with all licensing and copyright restrictions.*

## 3. Technical Architecture Overview

The system will consist of three main components:
1.  **Data Layer:** Cleaned and vectorized music corpus.
2.  **LLM Core:** Handles NLP understanding, retrieval (RAG), and response generation.
3.  **Application Layer:** User interface/API for input/output.

```mermaid
graph TD
    A[User Input: Text Query] --> B{LLM Gateway};
    B -- Semantic Query --> C[Vector Database (Embeddings)];
    B -- Factual Query --> D[Metadata Store (SQL/NoSQL)];
    C --> E[Retrieval Augmentation];
    D --> E;
    E --> F{Response Generator LLM};
    F --> G[Output: Playlist/Recommendation + Explanation];
    H[Music Data Sources] --> I[Data Ingestion Pipeline];
    I --> C;
    I --> D;
## 4. Phased Implementation Plan

### Phase 1: Setup and Data Preparation
1.  Research and finalize data sources.
2.  Set up core project structure and version control documentation (`docs/`).
3.  Develop the initial Data Ingestion Pipeline to clean and normalize metadata and lyrics.
4.  Implement the Vectorization Service (choosing an embedding model).
5.  Populate the Vector Database.

### Phase 2: Core Feature Implementation (Parallel Tracks)
**Track A: Semantic Playlist Generator**
1.  Develop sentiment/mood extraction module from lyrics/metadata using LLM prompts.
2.  Implement playlist construction logic based on extracted vectors (nearest neighbor search).

**Track B: Music Discovery Chatbot**
1.  Implement RAG system for factual lookups (artist info, riff analysis context).
2.  Develop prompt engineering for generating *explanations* for recommendations.

### Phase 3: Integration and Release
1.  Integrate Track A and Track B results into a unified application interface (API or simple web interface).
2.  Performance tuning and quality assurance targeting *nuanced recommendations*.
3.  Finalize and save all planning/design documents in `docs/`.