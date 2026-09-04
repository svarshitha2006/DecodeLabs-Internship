import pandas as pd

# Load the raw dataset
df = pd.read_excel("raw_dataset.xlsx")

# Display the first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Check unique values in text columns
print("\nProduct values:")
print(df["Product"].unique())

print("\nPayment Method values:")
print(df["PaymentMethod"].unique())

print("\nOrder Status values:")
print(df["OrderStatus"].unique())

print("\nReferral Source values:")
print(df["ReferralSource"].unique())

# Check numeric columns
print("\nNumeric columns summary:")
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe())

# Check TotalPrice calculation
df["CalculatedTotal"] = df["Quantity"] * df["UnitPrice"]

incorrect_rows = df[
    abs(df["TotalPrice"] - df["CalculatedTotal"]) > 0.01
]

print("\nTotal incorrect TotalPrice values:")
print(len(incorrect_rows))

print("\nFirst 10 incorrect rows:")
print(
    incorrect_rows[
        ["OrderID", "Quantity", "UnitPrice", "TotalPrice", "CalculatedTotal"]
    ].head(10)
)

# Check missing CouponCode values
print("\nMissing CouponCode examples:")
print(df[df["CouponCode"].isna()][["OrderID", "CouponCode"]].head(10))

# Fill missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Verify missing values are handled
print("\nMissing CouponCode after cleaning:")
print(df["CouponCode"].isnull().sum())

# Remove temporary calculation column
df = df.drop(columns=["CalculatedTotal"])

# Save cleaned dataset
df.to_excel("cleaned_dataset.xlsx", index=False)

print("\nCleaned dataset saved successfully!")