import pandas as pd
from load_data import load_raw
from cleaning import clean_order_data

print("Memulai load file...")

df = load_raw("History of Orders - East Indies CC - Desember.csv")

print("Berhasil load file!")
print(df.head())

# ========== CLEANING ==========
df = clean_order_data(df)

print("\nSetelah cleaning:")
print(df.dtypes)
print(df.head())

# ========== EDA DASAR ==========

print("\n===== 1. Summary Statistik =====")
print(df.describe(include="all"))

print("\n===== 2. Top 10 item paling sering dibeli =====")
top_qty = (
    df.groupby("Item Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_qty)

print("\n===== 3. Total spending per supplier =====")
supplier_spending = df.groupby("Supplier")["Total"].sum().sort_values(ascending=False)
supplier_spending = supplier_spending.apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))
print(supplier_spending)

print("\n===== 4. Spending per minggu =====")
week_spending = df.groupby("Week")["Total"].sum()
week_spending = week_spending.apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))
print(week_spending)

print("\n===== 5. Total pembelian per hari =====")
daily_spending = df.groupby("Date")["Total"].sum()
daily_spending = daily_spending.apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))
print(daily_spending)
