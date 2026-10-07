from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


RAW_DIR = Path("data/raw")
OUTPUT_FILE = RAW_DIR / "online_retail_ii.csv"


def download_dataset() -> pd.DataFrame:
    """Fetch UCI Online Retail II (dataset 502) and persist the raw features."""
    dataset = fetch_ucirepo(id=502)
    df = dataset.data.features.copy()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    return df


def main() -> None:
    df = download_dataset()
    print(f"Saved {len(df):,} rows to {OUTPUT_FILE}")
    print(f"Columns: {list(df.columns)}")


if __name__ == "__main__":
    main()
