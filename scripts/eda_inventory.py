import pandas as pd
from load_data import load_raw
from cleaning import clean_order_data


# ================================
# 1. LOAD DATA
# ================================
print("Memulai load file...")

df = load_raw("Receiving Report.csv", folder="receiving")

print("Berhasil load file!")
print(df.head())


# ================================
# 2. CLEANING
# ================================
df = clean_order_data(df)

# Tambahan kolom turunan waktu
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.strftime("%B")

print("\nSetelah cleaning:")
print(df.dtypes)
print(df.head())


# ================================
# 3. EDA
# ================================


#1. Summary statistik
print("\n===== 1. Summary Statistik =====")
print(df.describe(include="all"))

#2. Top 10 item paling sering dibeli
print("\n===== 2. Top 10 item paling sering dibeli =====")
top_qty = (
    df.groupby("Item Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_qty)
#3. Total spending per supplier
print("\n===== 3. Total spending per supplier =====")
supplier_spending = (
    df.groupby("Supplier")["Total"]
    .sum()
    .sort_values(ascending=False)
    .apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))
)
print(supplier_spending)


#4. Spending per minggu
print("\n===== 4. Spending per minggu =====")
week_spending = (
    df.groupby("Week")["Total"]
    .sum()
    .apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))
)
print(week_spending)

#5. Total pembelian per hari
print("\n===== 5. Total pembelian per hari =====")
daily_spending = (
    df.groupby("Date")["Total"]
    .sum()
    .apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))
)
print(daily_spending)

#6. Total pembelian per bulan
print("\n===== 6. Total pembelian per bulan =====")
monthly_spending = (
    df.groupby("Month")["Total"]
    .sum()
    .apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))
)
print(monthly_spending)

#7. Total pembelian rata-rata per transaksi di 3 bulan terakhir
print("\n===== 7. Total pembelian rata-rata per transaksi di 3 bulan terakhir =====")

month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

monthly_total = df.groupby("Month_Name")["Total"].sum()

avg_monthly_total = monthly_total.mean()

print("Rata-rata pembelian per bulan:", f"Rp {avg_monthly_total:,.0f}".replace(",", "."))

#8. Rata-rata pembelian per hari di bulan september
print("\n=== 8. Rata-rata pembelian per  di bulan september ===")
df_sep = df[df["Month"] == 9]

daily_sep = df_sep.groupby("Date")["Total"].sum()

avg_daily_sep = daily_sep.mean()

print("Total pembelian September:", f"Rp {daily_sep.sum():,.0f}".replace(",", "."))
print("Jumlah hari dengan transaksi:", len(daily_sep))
print("Rata-rata pembelian per hari di September:", f"Rp {avg_daily_sep:,.0f}".replace(",", "."))

#9. Rata-rata pembelian per hari di bulan oktober
print("\n=== 9. Rata-rata pembelian per  di bulan oktober ===")
df_oct = df[df["Month"] == 10]

daily_oct = df_oct.groupby("Date")["Total"].sum()

avg_daily_oct = daily_oct.mean()

print("Total pembelian October:", f"Rp {daily_oct.sum():,.0f}".replace(",", "."))
print("Jumlah hari dengan transaksi:", len(daily_oct))
print("Rata-rata pembelian per hari di October:", f"Rp {avg_daily_oct:,.0f}".replace(",", "."))

#10. Rata-rata pembelian per hari di bulan november
print("\n=== 10. Rata-rata pembelian per  di bulan november ===")
df_nov = df[df["Month"] == 11]

daily_nov = df_nov.groupby("Date")["Total"].sum()

avg_daily_nov = daily_nov.mean()
print("Total pembelian November:", f"Rp {daily_nov.sum():,.0f}".replace(",", "."))
print("Jumlah hari dengan transaksi:", len(daily_nov))
print("Rata-rata pembelian per hari di November:", f"Rp {avg_daily_nov:,.0f}".replace(",", "."))


#11. Rata-rata pembelian per hari di kategori reguler kitchen
print("\n=== 11. Rata-rata pembelian kategori reguler kitchen ===")

df["Category"] = df["Category"].str.strip().str.lower()
df_kitchen = df[df["Category"].str.lower() == "reguler kitchen"]

daily_kitchen= df_kitchen.groupby("Date")["Total"].sum()

total_kitchen = df_kitchen["Total"].sum()
avg_daily_kitchen = daily_kitchen.mean()

print("Total pembelian Reguler Kitchen:", f"Rp {daily_kitchen.sum():,.0f}".replace(",", "."))
print("Jumlah hari dengan transaksi:", len(daily_kitchen))
print("Rata-rata pembelian per hari di Reguler Kitchen:", f"Rp {avg_daily_kitchen:,.0f}".replace(",", "."))

print("\n=== 12. Rata-rata pembelian kategori staff meals ===")

df["Category"] = df["Category"].str.strip().str.lower()
df_staff_meals = df[df["Category"].str.lower() == "staff meals"]

daily_staff_meals= df_staff_meals.groupby("Date")["Total"].sum()

total_staff_meals = df_staff_meals["Total"].sum()
avg_daily_staff_meals = daily_staff_meals.mean()

print("Total pembelian Staff Meals:", f"Rp {daily_staff_meals.sum():,.0f}".replace(",", "."))
print("Jumlah hari dengan transaksi:", len(daily_staff_meals))
print("Rata-rata pembelian per hari di Staff Meals:", f"Rp {avg_daily_staff_meals:,.0f}".replace(",", "."))