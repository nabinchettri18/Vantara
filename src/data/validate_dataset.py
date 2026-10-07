from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "Invoice",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "Price",
    "Customer ID",
    "Country",
}


def validate_dataset(path: str | Path) -> dict[str, object]:
    """Run non-destructive Day 1 validation checks on the raw dataset."""
    df = pd.read_csv(path)
    missing_columns = sorted(REQUIRED_COLUMNS - set(df.columns))

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_columns": missing_columns,
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_customer_id": int(df["Customer ID"].isna().sum()),
        "unique_customers": int(df["Customer ID"].nunique(dropna=True)),
        "unique_invoices": int(df["Invoice"].nunique(dropna=True)),
        "negative_quantity_rows": int((df["Quantity"] < 0).sum()),
        "non_positive_price_rows": int((df["Price"] <= 0).sum()),
    }


if __name__ == "__main__":
    result = validate_dataset("data/raw/online_retail_ii.csv")
    for key, value in result.items():
        print(f"{key}: {value}")
