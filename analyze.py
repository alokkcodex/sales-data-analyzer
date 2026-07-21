"""
Sales Data Analyzer
--------------------
A small end-to-end data analysis project built with pandas and matplotlib.

It answers a few common business questions a Data Analyst is asked:
1. Which region generates the most revenue?
2. Which product category sells the most units?
3. How does revenue trend over time?
4. Who are the top 5 best-selling products?

Run:
    python analyze.py

Outputs:
    Console summary + 3 charts saved in the outputs/ folder
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = os.path.join("data", "sales_data.csv")
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"])
    return df


def revenue_by_region(df: pd.DataFrame):
    result = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
    print("\nRevenue by Region:")
    print(result)

    plt.figure(figsize=(6, 4))
    result.plot(kind="bar", color="#4C72B0")
    plt.title("Total Revenue by Region")
    plt.ylabel("Revenue (₹)")
    plt.xlabel("Region")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "revenue_by_region.png"))
    plt.close()
    return result


def units_by_category(df: pd.DataFrame):
    result = df.groupby("Category")["Units Sold"].sum().sort_values(ascending=False)
    print("\nUnits Sold by Category:")
    print(result)

    plt.figure(figsize=(6, 4))
    result.plot(kind="pie", autopct="%1.1f%%", ylabel="")
    plt.title("Units Sold by Category")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "units_by_category.png"))
    plt.close()
    return result


def revenue_trend(df: pd.DataFrame):
    monthly = df.set_index("Date").resample("ME")["Revenue"].sum()
    print("\nMonthly Revenue Trend:")
    print(monthly)

    plt.figure(figsize=(6, 4))
    monthly.plot(kind="line", marker="o", color="#DD8452")
    plt.title("Monthly Revenue Trend")
    plt.ylabel("Revenue (₹)")
    plt.xlabel("Month")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "monthly_revenue_trend.png"))
    plt.close()
    return monthly


def top_products(df: pd.DataFrame, n: int = 5):
    result = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(n)
    print(f"\nTop {n} Products by Revenue:")
    print(result)
    return result


def main():
    df = load_data(DATA_PATH)

    print("=" * 50)
    print("SALES DATA ANALYSIS REPORT")
    print("=" * 50)
    print(f"Total records: {len(df)}")
    print(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"Total revenue: ₹{df['Revenue'].sum():,}")

    revenue_by_region(df)
    units_by_category(df)
    revenue_trend(df)
    top_products(df)

    print("\nCharts saved in the 'outputs/' folder.")


if __name__ == "__main__":
    main()
