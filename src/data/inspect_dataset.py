from ucimlrepo import fetch_ucirepo


def main() -> None:
    dataset = fetch_ucirepo(id=502)
    df = dataset.data.features

    print("=== VANTARA DAY 1 DATASET INSPECTION ===")
    print(f"Shape: {df.shape}")
    print("\nColumns:")
    for column in df.columns:
        print(f" - {column}")

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum())

    print(f"\nUnique customers: {df['Customer ID'].nunique(dropna=True)}")
    print(f"Unique invoices: {df['Invoice'].nunique(dropna=True)}")
    print(f"Date range: {df['InvoiceDate'].min()} -> {df['InvoiceDate'].max()}")
    print(f"Negative quantity rows: {(df['Quantity'] < 0).sum()}")
    print(f"Non-positive price rows: {(df['Price'] <= 0).sum()}")


if __name__ == "__main__":
    main()
