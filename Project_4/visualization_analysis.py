import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# DecodeLabs - Project 4
# Data Visualization
# ============================================

# Load dataset
df = pd.read_excel("cleaned_dataset.xlsx")

# Create output folder
import os
os.makedirs("output", exist_ok=True)

print("=" * 60)
print("DecodeLabs - Project 4: Data Visualization")
print("=" * 60)

print(f"\nDataset Shape: {df.shape}")
print(f"Records: {len(df)}")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# ============================================
# 1. ORDERS BY PRODUCT
# ============================================

product_orders = df["Product"].value_counts().sort_values(ascending=True)

plt.figure(figsize=(10, 6))
bars = plt.barh(
    product_orders.index,
    product_orders.values,
    color="#4C78A8"
)

plt.title(
    "Printer Leads Product Orders While Phone Has the Fewest",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Number of Orders")
plt.ylabel("Product")

for bar in bars:
    plt.text(
        bar.get_width() + 2,
        bar.get_y() + bar.get_height() / 2,
        f"{int(bar.get_width())}",
        va="center"
    )

plt.tight_layout()
plt.savefig(
    "output/01_orders_by_product.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================
# 2. REVENUE BY PRODUCT
# ============================================

revenue_product = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 6))
bars = plt.barh(
    revenue_product.index,
    revenue_product.values,
    color="#F28E2B"
)

plt.title(
    "Chair Generates the Highest Product Revenue",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Total Revenue")
plt.ylabel("Product")

for bar in bars:
    plt.text(
        bar.get_width() + 3000,
        bar.get_y() + bar.get_height() / 2,
        f"₹{bar.get_width():,.0f}",
        va="center"
    )

plt.tight_layout()
plt.savefig(
    "output/02_revenue_by_product.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================
# 3. MONTHLY ORDER TREND
# ============================================

monthly_orders = (
    df.set_index("Date")
    .resample("ME")
    .size()
)

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_orders.index,
    monthly_orders.values,
    marker="o",
    linewidth=2,
    color="#59A14F"
)

plt.title(
    "Monthly Order Volume Shows Strong Variation Over Time",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "output/03_monthly_order_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================
# 4. MONTHLY REVENUE TREND
# ============================================

monthly_revenue = (
    df.set_index("Date")["TotalPrice"]
    .resample("ME")
    .sum()
)

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o",
    linewidth=2,
    color="#E45756"
)

plt.title(
    "Monthly Revenue Peaks in June 2024",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "output/04_monthly_revenue_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================
# 5. PAYMENT METHOD DISTRIBUTION
# ============================================

payment_counts = df["PaymentMethod"].value_counts()

plt.figure(figsize=(8, 8))

colors = [
    "#4C78A8",
    "#F28E2B",
    "#59A14F",
    "#E45756",
    "#B279A2"
]

plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors
)

plt.title(
    "Online Payment Is the Most Frequently Used Method",
    fontsize=14,
    fontweight="bold"
)

plt.tight_layout()
plt.savefig(
    "output/05_payment_method_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================
# 6. ORDER STATUS DISTRIBUTION
# ============================================

status_counts = df["OrderStatus"].value_counts().sort_values()

plt.figure(figsize=(10, 6))

bars = plt.barh(
    status_counts.index,
    status_counts.values,
    color="#76B7B2"
)

plt.title(
    "Cancelled and Returned Orders Form a Large Share of Statuses",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Number of Orders")
plt.ylabel("Order Status")

for bar in bars:
    plt.text(
        bar.get_width() + 2,
        bar.get_y() + bar.get_height() / 2,
        f"{int(bar.get_width())}",
        va="center"
    )

plt.tight_layout()
plt.savefig(
    "output/06_order_status_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================
# 7. QUANTITY VS TOTAL PRICE
# ============================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Quantity"],
    df["TotalPrice"],
    alpha=0.6,
    color="#B279A2"
)

plt.title(
    "Higher Quantities Are Associated With Higher Order Values",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Quantity")
plt.ylabel("Total Price")

plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(
    "output/07_quantity_vs_total_price.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# ============================================
# COMPLETION MESSAGE
# ============================================

print("\n7 visualizations created successfully!")

print("\nOutput files:")
print("1. 01_orders_by_product.png")
print("2. 02_revenue_by_product.png")
print("3. 03_monthly_order_trend.png")
print("4. 04_monthly_revenue_trend.png")
print("5. 05_payment_method_distribution.png")
print("6. 06_order_status_distribution.png")
print("7. 07_quantity_vs_total_price.png")

print("\n" + "=" * 60)
print("ALL VISUALIZATIONS COMPLETED SUCCESSFULLY!")
print("=" * 60)