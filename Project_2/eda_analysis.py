import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_excel("cleaned_dataset.xlsx")

# Create output folder
output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

print("Dataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())


# ============================================================
# 2. BASIC STATISTICS
# ============================================================

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

print("\n================ BASIC STATISTICS ================")

print("\nCount:")
print(df[numeric_columns].count())

print("\nMean:")
print(df[numeric_columns].mean())

print("\nMedian:")
print(df[numeric_columns].median())


# ============================================================
# 3. HIGHEST AND LOWEST ORDERS
# ============================================================

print("\n================ HIGHEST 10 ORDERS ================")

highest_orders = (
    df[["OrderID", "Product", "Quantity", "TotalPrice"]]
    .sort_values("TotalPrice", ascending=False)
    .head(10)
)

print(highest_orders)


print("\n================ LOWEST 10 ORDERS ================")

lowest_orders = (
    df[["OrderID", "Product", "Quantity", "TotalPrice"]]
    .sort_values("TotalPrice", ascending=True)
    .head(10)
)

print(lowest_orders)


# ============================================================
# 4. OUTLIER ANALYSIS - IQR
# ============================================================

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower_bound) |
    (df["TotalPrice"] > upper_bound)
]

print("\n================ IQR OUTLIER ANALYSIS ================")

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of Outliers:", len(outliers))

print("\nOutlier Orders:")
print(
    outliers[
        ["OrderID", "Product", "Quantity", "TotalPrice"]
    ]
)


# ============================================================
# 5. YEARLY TREND
# ============================================================

df["Year"] = df["Date"].dt.year

yearly_orders = df.groupby("Year").size()

print("\n================ ORDERS BY YEAR ================")
print(yearly_orders)


# ============================================================
# 6. MONTHLY TREND
# ============================================================

df["Month"] = df["Date"].dt.month

monthly_orders = df.groupby("Month").size()

print("\n================ ORDERS BY MONTH ================")
print(monthly_orders)


# ============================================================
# 7. PRODUCT ANALYSIS
# ============================================================

product_orders = df["Product"].value_counts()

print("\n================ ORDERS BY PRODUCT ================")
print(product_orders)


# ============================================================
# 8. REVENUE BY PRODUCT
# ============================================================

product_revenue = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n================ REVENUE BY PRODUCT ================")
print(product_revenue)


# ============================================================
# 9. PAYMENT METHOD ANALYSIS
# ============================================================

payment_counts = df["PaymentMethod"].value_counts()

print("\n================ ORDERS BY PAYMENT METHOD ================")
print(payment_counts)


# ============================================================
# 10. ORDER STATUS ANALYSIS
# ============================================================

status_counts = df["OrderStatus"].value_counts()

print("\n================ ORDERS BY ORDER STATUS ================")
print(status_counts)


# ============================================================
# 11. CORRELATION ANALYSIS
# ============================================================

correlation = df[numeric_columns].corr()

print("\n================ CORRELATION MATRIX ================")
print(correlation)


# ============================================================
# 12. CHART 1 - TOTAL PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["TotalPrice"],
    bins=20,
    color="#4C78A8",
    edgecolor="white"
)

plt.title(
    "Distribution of Total Order Price",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Total Price")
plt.ylabel("Number of Orders")

plt.grid(axis="y", alpha=0.25)

plt.tight_layout()

plt.savefig(
    output_folder / "01_total_price_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 13. CHART 2 - MONTHLY ORDER TREND
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_orders.index,
    monthly_orders.values,
    marker="o",
    linewidth=3,
    color="#E45756",
    markerfacecolor="#F2CF5B",
    markeredgecolor="#E45756",
    markersize=8
)

plt.title(
    "Monthly Order Trend",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(range(1, 13))

plt.grid(alpha=0.25)

plt.tight_layout()

plt.savefig(
    output_folder / "02_monthly_order_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 14. CHART 3 - ORDERS BY PRODUCT
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    product_orders.index,
    product_orders.values,
    color="#59A14F",
    edgecolor="white"
)

plt.title(
    "Number of Orders by Product",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.xticks(rotation=20)

plt.grid(axis="y", alpha=0.25)

plt.tight_layout()

plt.savefig(
    output_folder / "03_orders_by_product.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 15. CHART 4 - REVENUE BY PRODUCT
# ============================================================

plt.figure(figsize=(10, 6))

plt.barh(
    product_revenue.index,
    product_revenue.values,
    color="#F28E2B",
    edgecolor="white"
)

plt.title(
    "Revenue by Product",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Total Revenue")
plt.ylabel("Product")

plt.grid(axis="x", alpha=0.25)

plt.tight_layout()

plt.savefig(
    output_folder / "04_revenue_by_product.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 16. CHART 5 - PAYMENT METHOD
# ============================================================

plt.figure(figsize=(9, 7))

payment_colors = [
    "#76B7B2",
    "#EDC948",
    "#AF7AA1",
    "#FF9DA7",
    "#9C755F"
]

plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=payment_colors,
    wedgeprops={"edgecolor": "white"}
)

plt.title(
    "Orders by Payment Method",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    output_folder / "05_orders_by_payment_method.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 17. CHART 6 - ORDER STATUS
# ============================================================

plt.figure(figsize=(10, 6))

status_colors = [
    "#E15759",
    "#B279A2",
    "#9D9D9D",
    "#4E79A7",
    "#59A14F"
]

plt.bar(
    status_counts.index,
    status_counts.values,
    color=status_colors,
    edgecolor="white"
)

plt.title(
    "Orders by Order Status",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.xticks(rotation=20)

plt.grid(axis="y", alpha=0.25)

plt.tight_layout()

plt.savefig(
    output_folder / "06_orders_by_status.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 18. CHART 7 - CORRELATION MATRIX
# ============================================================

plt.figure(figsize=(9, 7))

plt.imshow(
    correlation,
    cmap="coolwarm",
    aspect="auto",
    vmin=-1,
    vmax=1
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=30,
    ha="right"
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title(
    "Correlation Matrix",
    fontsize=16,
    fontweight="bold"
)

# Add correlation values inside the matrix
for i in range(len(correlation)):
    for j in range(len(correlation)):
        plt.text(
            j,
            i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center",
            fontsize=10
        )

plt.tight_layout()

plt.savefig(
    output_folder / "07_correlation_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 19. FINISH
# ============================================================

print("\n================================================")
print("ALL EDA ANALYSIS AND CHARTS COMPLETED!")
print("================================================")

print("\nCharts saved in the 'output' folder:")
print("1. 01_total_price_distribution.png")
print("2. 02_monthly_order_trend.png")
print("3. 03_orders_by_product.png")
print("4. 04_revenue_by_product.png")
print("5. 05_orders_by_payment_method.png")
print("6. 06_orders_by_status.png")
print("7. 07_correlation_matrix.png")