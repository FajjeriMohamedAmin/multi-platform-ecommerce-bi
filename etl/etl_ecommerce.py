import pandas as pd


df = pd.read_csv("../data_raw/ecommerce_10000.csv")


df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]


df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")


numeric_cols = ["price", "quantity", "totalamount", "rating", "reviews"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


df["rating"] = df["rating"].fillna(df["rating"].mean())
df["reviews"] = df["reviews"].fillna(0)


df = df.dropna(subset=["price", "quantity", "orderdate"])


df = df.drop_duplicates(subset=["orderid"])


df["recalculated_total"] = df["price"] * df["quantity"]


df["order_year"] = df["orderdate"].dt.year
df["order_month"] = df["orderdate"].dt.month


df.to_csv("../data_cleaned/ecommerce_cleaned.csv", index=False)

print("ETL process completed successfully.")

