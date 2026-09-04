# Data Cleaning & Preparation

## Project Overview

This project focuses on cleaning and preparing an e-commerce order dataset for analysis.

The raw dataset contains 1,200 records and 14 columns.

## Dataset Columns

- OrderID
- Date
- CustomerID
- Product
- Quantity
- UnitPrice
- ShippingAddress
- PaymentMethod
- OrderStatus
- TrackingNumber
- ItemsInCart
- CouponCode
- ReferralSource
- TotalPrice

## Data Quality Checks

### 1. Missing Values

The `CouponCode` column contained 309 missing values.

These missing values were replaced with:

`No Coupon`

After cleaning, there are 0 missing values in the `CouponCode` column.

### 2. Duplicate Records

The dataset contained 0 duplicate records.

No rows were removed for duplication.

### 3. Data Formats

The following data types were checked:

- Date → datetime format
- Quantity → integer
- UnitPrice → decimal/float
- ItemsInCart → integer
- TotalPrice → decimal/float

The data types were found to be appropriate.

### 4. Text Consistency

The Product, PaymentMethod, OrderStatus, and ReferralSource columns were checked for inconsistent text values.

No obvious inconsistencies were found.

### 5. Total Price Validation

The `TotalPrice` column was checked against:

`Quantity × UnitPrice`

All records passed the validation check.

## Cleaning Summary

| Check | Result |
|---|---|
| Total Records | 1,200 |
| Missing CouponCode | 309 → 0 |
| Duplicate Records | 0 |
| Text Inconsistencies | None found |
| Invalid Numeric Values | None found |
| TotalPrice Errors | 0 |

## Files

- `raw_dataset.xlsx` – Original dataset
- `cleaned_dataset.xlsx` – Cleaned dataset
- `clean_dataset.py` – Python script used for data cleaning

## Tools Used

- Python
- Pandas
- OpenPyXL
- VS Code